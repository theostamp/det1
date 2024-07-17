import cv2
import os
import json
from PySide6.QtWidgets import QMessageBox, QApplication, QMainWindow, QFileDialog, QGraphicsScene, QMenu
from PySide6.QtGui import QPixmap, QImage, QColor
from PySide6.QtCore import Qt, QPointF
from annotation_ui import Ui_MainWindow  # Εισαγωγή της παραγόμενης κλάσης από το Qt Designer

class ImageAnnotator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # Δημιουργία αντικειμένου της παραγόμενης κλάσης UI
        self.ui.setupUi(self)  # Σύνδεση του UI με το κύριο παράθυρο

        self.image_path = None
        self.annotated_image = None
        self.annotations = []
        self.drawing = False
        self.start_point = None
        self.end_point = None
        self.image_scale_factor = 1.0
        self.image_offset = (0, 0)
        self.selected_annotation_index = None
        self.resizing = False
        self.moving = False
        self.resize_margin = 5  # Μικρότερες διαστάσεις για το χειριστήριο
        self.current_handler = None
        self.allow_drawing = True

        self.ui.pushButton_load_image.clicked.connect(self.load_image_dialog)
        self.ui.pushButton_save_annotations.clicked.connect(self.save_annotations)
        self.ui.pushButton_delete_rest.clicked.connect(self.start_deleting)

        self.ui.graphicsView.setMouseTracking(True)
        self.ui.graphicsView.mousePressEvent = self.mouse_press_event
        self.ui.graphicsView.mouseMoveEvent = self.mouse_move_event
        self.ui.graphicsView.mouseReleaseEvent = self.mouse_release_event

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete and self.selected_annotation_index is not None:
            self.delete_selected_annotation()
    
    def load_image_dialog(self):
        try:
            file_dialog = QFileDialog(self)
            file_path, _ = file_dialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.bmp)")
            if file_path:
                self.image_path = file_path
                self.load_image()
                self.ui.pushButton_save_annotations.setEnabled(True)
        except Exception as e:
            print(f"Error loading image: {e}")

    def load_image(self):
        try:
            if self.image_path:
                image = cv2.imread(self.image_path)
                self.annotated_image = self.resize_image(image, width=640)

                height, width, channel = self.annotated_image.shape
                bytes_per_line = 3 * width
                q_img = QImage(self.annotated_image.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
                pixmap = QPixmap.fromImage(q_img)

                self.scene = QGraphicsScene(self)
                self.scene.addPixmap(pixmap)
                self.ui.graphicsView.setScene(self.scene)
                self.ui.graphicsView.setSceneRect(0, 0, width, height)

                self.image_scale_factor = image.shape[1] / self.annotated_image.shape[1]
                self.image_offset = ((self.ui.graphicsView.width() - pixmap.width()) // 2,
                                     (self.ui.graphicsView.height() - pixmap.height()) // 2)
        except Exception as e:
            print(f"Error setting up image: {e}")

    def mouse_press_event(self, event):
        try:
            pos = self.map_to_image_coordinates(event.position())
            clicked_on_handler = False
            clicked_on_annotation = False

            if event.button() == Qt.LeftButton:
                for i, (start, end) in enumerate(self.annotations):
                    handler = self.point_on_handler(pos, start, end)
                    if handler:
                        self.selected_annotation_index = i
                        self.current_handler = handler
                        self.resizing = True
                        clicked_on_handler = True
                        break
                    elif self.point_in_rect(pos, start, end):
                        self.selected_annotation_index = i
                        self.moving = True
                        self.start_point = pos
                        clicked_on_annotation = True
                        break

                if clicked_on_handler or clicked_on_annotation:
                    self.update_display_image()
                else:
                    self.start_point = pos
                    self.drawing = True
            elif event.button() == Qt.RightButton:
                for i, (start, end) in enumerate(self.annotations):
                    if self.point_in_rect(pos, start, end):
                        self.selected_annotation_index = i
                        self.show_context_menu(event.globalPos())
                        return
        except Exception as e:
            print(f"Error in mouse press event: {e}")

    def mouse_move_event(self, event):
        try:
            if self.drawing:
                self.end_point = self.map_to_image_coordinates(event.position())
                self.update_display_image()
            elif self.moving and self.selected_annotation_index is not None:
                delta = self.map_to_image_coordinates(event.position())
                dx = delta[0] - self.start_point[0]
                dy = delta[1] - self.start_point[1]
                start, end = self.annotations[self.selected_annotation_index]
                self.annotations[self.selected_annotation_index] = (
                    (start[0] + dx, start[1] + dy),
                    (end[0] + dx, end[1] + dy)
                )
                self.start_point = delta
                self.update_display_image()
            elif self.resizing and self.selected_annotation_index is not None and self.current_handler:
                self.end_point = self.map_to_image_coordinates(event.position())
                start, end = self.annotations[self.selected_annotation_index]

                # Περιορισμός του κάτω δεξιού χειριστηρίου να μην υπερβαίνει τα όρια αριστερά και πάνω
                self.end_point = (
                    max(start[0] + 1, self.end_point[0]),
                    max(start[1] + 1, self.end_point[1])
                )

                self.annotations[self.selected_annotation_index] = (self.normalize_coordinates(start, self.end_point))
                self.update_display_image()
        except Exception as e:
            print(f"Error in mouse move event: {e}")

    def mouse_release_event(self, event):
        try:
            if event.button() == Qt.LeftButton and self.drawing:
                self.drawing = False
                self.end_point = self.map_to_image_coordinates(event.position())
                if not self.annotation_intersects_existing(self.start_point, self.end_point):
                    self.annotations.append(self.normalize_coordinates(self.start_point, self.end_point))
                self.update_display_image(finalize=True)
            elif event.button() == Qt.LeftButton and self.moving:
                self.moving = False
                self.selected_annotation_index = None
                self.allow_drawing = True
                self.update_display_image()
            elif event.button() == Qt.LeftButton and self.resizing:
                self.resizing = False
                self.selected_annotation_index = None
                self.current_handler = None
                self.allow_drawing = True
                self.update_display_image()
        except Exception as e:
            print(f"Error in mouse release event: {e}")

    def normalize_coordinates(self, start, end):
        x1, y1 = start
        x2, y2 = end
        start = (min(x1, x2), min(y1, y2))
        end = (max(x1, x2), max(y1, y2))
        return start, end

    def show_context_menu(self, position):
        try:
            menu = QMenu(self)
            delete_action = menu.addAction("Διαγραφή")

            action = menu.exec_(position)
            if action == delete_action:
                self.delete_selected_annotation()
                self.allow_drawing = True
        except Exception as e:
            print(f"Error showing context menu: {e}")

    def delete_selected_annotation(self):
        try:
            if self.selected_annotation_index is not None:
                del self.annotations[self.selected_annotation_index]
                self.selected_annotation_index = None
                self.update_display_image()
        except Exception as e:
            print(f"Error deleting annotation: {e}")

    def start_deleting(self):
        try:
            if self.selected_annotation_index is not None:
                self.delete_selected_annotation()
            self.allow_drawing = True
        except Exception as e:
            print(f"Error starting deletion: {e}")

    def map_to_image_coordinates(self, pos):
        x = (pos.x() - self.image_offset[0]) * self.image_scale_factor
        y = (pos.y() - self.image_offset[1]) * self.image_scale_factor
        return int(x), int(y)

    def point_in_rect(self, point, start, end):
        x, y = point
        return start[0] <= x <= end[0] and start[1] <= y <= end[1]

    def annotation_intersects_existing(self, start, end):
        for (existing_start, existing_end) in self.annotations:
            if self.rects_intersect((start, end), (existing_start, existing_end)):
                return True
        return False

    def rects_intersect(self, rect1, rect2):
        (x1_start, y1_start), (x1_end, y1_end) = rect1
        (x2_start, y2_start), (x2_end, y2_end) = rect2
        return not (x1_end < x2_start or x1_start > x2_end or y1_end < y2_start or y1_start > y2_end)

    def point_on_handler(self, point, start, end):
        x, y = point
        if abs(x - end[0]) <= self.resize_margin and abs(y - end[1]) <= self.resize_margin:
            return "bottom-right"
        return None

    def update_display_image(self, finalize=False):
        try:
            display_image = self.annotated_image.copy()

            for i, (start, end) in enumerate(self.annotations):
                color = (0, 0, 255) if i == self.selected_annotation_index else (0, 255, 0)
                fill_color = (0, 0, 255, 50) if i == self.selected_annotation_index else (0, 255, 0, 50)  # Ημιδιαφανές γέμισμα
                cv2.rectangle(display_image, start, end, fill_color, thickness=-1)  # Γέμισμα πλαισίου
                cv2.rectangle(display_image, start, end, color, 1)  # Λεπτή γραμμή για τα πλαίσια
                cv2.putText(display_image, str(i + 1), (end[0], end[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
                # Προσθήκη χειριστηρίου στην κάτω δεξιά γωνία
                cv2.rectangle(display_image, (end[0] - self.resize_margin, end[1] - self.resize_margin), 
                              (end[0] + self.resize_margin, end[1] + self.resize_margin), color, -1)

            if self.drawing and self.start_point and self.end_point:
                start, end = self.normalize_coordinates(self.start_point, self.end_point)
                cv2.rectangle(display_image, start, end, (0, 255, 0), 1)
                if finalize:
                    cv2.putText(display_image, str(len(self.annotations)), (end[0], end[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

            height, width, channel = display_image.shape
            bytes_per_line = 3 * width
            q_img = QImage(display_image.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
            self.scene.clear()
            self.scene.addPixmap(QPixmap.fromImage(q_img))
            self.ui.graphicsView.setScene(self.scene)
        except Exception as e:
            print(f"Error updating display image: {e}")

    def save_annotations(self):
        action = self.confirm_save()

        if action == "cancel":
            return  # Ακύρωση της αποθήκευσης
        # Διαγραφή του παλιού αρχείου αν επιλέξει "Αντικατάσταση"
        if action == "replace":
            if os.path.exists('tables.txt'):
                print("Διαγράφεται το αρχείο tables.txt")
                os.remove('tables.txt')
            else:
                print("Το αρχείο tables.txt δεν βρέθηκε.")

        # Αποθήκευση των συντεταγμένων στο νέο αρχείο tables.txt
        with open('tables.txt', 'w') as file:
            for i, (start, end) in enumerate(self.annotations, start=1):
                x1, y1 = start
                x2, y2 = end
                line = f'{i} {x1} {y1} {x2} {y2}\n'
                file.write(line)

        # Αφαίρεση των οδηγιών από την εικόνα πριν την αποθήκευση
        self.annotated_image = cv2.imread(self.image_path) # type: ignore
        for i, (start, end) in enumerate(self.annotations, start=1):
            cv2.rectangle(self.annotated_image, start, end, (0, 255, 0), 2)
            # Προσθήκη αριθμού τραπεζιού στην εικόνα
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 1
            font_color = (255, 255, 255)
            text_position = (start[0], start[1] - 10)  # Λίγο πάνω από το πλαίσιο
            cv2.putText(self.annotated_image, str(i), text_position, font, font_scale, font_color, 2)

        # Αποθήκευση της τροποποιημένης εικόνας ως tables_init.jpg
        cv2.imwrite('tables_init.jpg', self.annotated_image)
        self.update_image('tables_init.jpg')

        # Εμφάνιση μηνύματος επιτυχίας
        QMessageBox.information(self, "Επιτυχία", "Η εργασία αποθηκεύτηκε. Μπορείτε να κλείσετε το παράθυρο.")

    def confirm_save(self):
        # Placeholder για τη μέθοδο επιβεβαίωσης αποθήκευσης
        # Θα πρέπει να υλοποιήσετε το GUI για την επιλογή της επιβεβαίωσης
        return "replace"  # Επιστρέφει "replace" ή "cancel"

    def resize_image(self, image, width=None, height=None, inter=cv2.INTER_AREA):
        try:
            dim = None
            (h, w) = image.shape[:2]

            if width is None and height is None:
                return image

            if width is None:
                r = height / float(h)
                dim = (int(w * r), height)
            else:
                r = width / float(w)
                dim = (width, int(h * r))

            resized = cv2.resize(image, dim, interpolation=inter)
            return resized
        except Exception as e:
            print(f"Error resizing image: {e}")

    def update_image(self, image_path):
        try:
            self.load_image()
        except Exception as e:
            print(f"Error updating image: {e}")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = ImageAnnotator()
    window.show()
    sys.exit(app.exec())
