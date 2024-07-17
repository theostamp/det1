import sys
import sqlite3
import qrcode
from PySide6.QtWidgets import QApplication,  QMainWindow, QMessageBox, QLabel, QScrollArea, QVBoxLayout, QWidget,QGridLayout,QFrame
from PySide6.QtGui import QPixmap
from waiters_ui import Ui_MainWindow  # Υποθέτοντας ότι η παραπάνω κλάση ονομάζεται ui_mainwindow.py
from PySide6.QtCore import QByteArray, QBuffer, QIODevice, Qt
from PySide6.QtWidgets import QApplication, QMainWindow,   QMessageBox, QLabel, QScrollArea, QVBoxLayout, QWidget, QGridLayout, QFrame, QListView
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QStringListModel
import sys
import sqlite3
import qrcode
from PySide6.QtGui import QPixmap, QImage


def create_database():
    conn = sqlite3.connect('waiters.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS waiters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            nickname TEXT NOT NULL,
            qr_code TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

create_database()

def load_qr_codes():
    conn = sqlite3.connect('waiters.db')
    c = conn.cursor()
    c.execute('SELECT name, surname, nickname, qr_code FROM waiters')
    waiters = c.fetchall()
    conn.close()
    return waiters

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, username='default_username'):
        super().__init__()
        self.username = username
        self.setupUi(self)
        self.setupListView()
        self.setupDeleteButton()
        self.pushButton.clicked.connect(self.create_waiter)
        # self.setup_qr_display()
        self.test_generate_qr()
       
    def test_generate_qr(self):
        test_data = "Hello, QR!"
        pixmap = self.generate_qr(test_data)
        if pixmap:
            print("QR Code generated successfully.")
        else:
            print("Failed to generate QR Code.")

    def setupListView(self):
        # self.listView_waiters = QListView(self.frame_2)
        self.listView_waiters.setObjectName(u"listView_waiters")
        self.model = QStringListModel(self)
        self.listView_waiters.setModel(self.model)
        self.updateListView()
        self.listView_waiters.clicked.connect(self.display_selected_qr_code)

    def setupDeleteButton(self):
        # self.pushButton_delete_waiter = QPushButton("Delete Waiter", self.frame_2)
        self.pushButton_delete_waiter.setObjectName(u"pushButton_delete_waiter")
        self.pushButton_delete_waiter.clicked.connect(self.deleteSelectedWaiter)


    def deleteSelectedWaiter(self):
        index = self.listView_waiters.currentIndex()
        if not index.isValid():
            QMessageBox.warning(self, "Selection Error", "Please select a waiter to delete.")
            return
        
        confirmation = QMessageBox.question(self, "Confirm Deletion", "Are you sure you want to delete this waiter?")
        if confirmation == QMessageBox.Yes:
            waiter_name = self.model.data(index, Qt.DisplayRole)
            self.removeWaiterFromDatabase(waiter_name)
            self.updateListView()
            self.clearQrDisplay()  # Καθαρισμός του QR placeholder


    def clearQrDisplay(self):
        self.QrPlaceholder.clear()  # Καθαρισμός του QLabel



    def removeWaiterFromDatabase(self, name):
        conn = sqlite3.connect('waiters.db')
        c = conn.cursor()
        c.execute('DELETE FROM waiters WHERE name=?', (name,))
        conn.commit()
        conn.close()

    def updateListView(self):
        conn = sqlite3.connect('waiters.db')
        c = conn.cursor()
        c.execute('SELECT name FROM waiters')
        names = c.fetchall()
        self.model.setStringList([name[0] for name in names])
        conn.close()



    def display_selected_qr_code(self, index):
        if not index.isValid():
            self.Waiter_name.setText("")  # Καθαρίζει το label αν η επιλογή δεν είναι έγκυρη
            self.QrPlaceholder.clear()  # Καθαρισμός του placeholder αν δεν υπάρχει έγκυρη επιλογή
            return

        name = self.model.data(index, Qt.DisplayRole)
        conn = sqlite3.connect('waiters.db')
        c = conn.cursor()
        c.execute('SELECT qr_code FROM waiters WHERE name=?', (name,))
        qr_code_data = c.fetchone()
        conn.close()

        if qr_code_data:
            qr_code = qr_code_data[0]
            qr_pixmap = self.generate_qr(qr_code)
            self.QrPlaceholder.setPixmap(qr_pixmap)
            self.Waiter_name.setText(name)  # Ενημερώνει το QLabel με το επιλεγμένο όνομα
        else:
            self.QrPlaceholder.clear()  # Καθαρισμός του placeholder αν δεν βρεθεί QR code
            self.Waiter_name.setText("")  # Καθαρίζει το label αν δεν υπάρχει σερβιτόρος



    def create_waiter(self):
        name = self.lineEdit.text()
        surname = self.lineEdit_2.text()
        nickname = self.lineEdit_3.text()
        
        if not name:
            QMessageBox.warning(self, "Error", "Please provide a name.")
            return
        
        qr_data = f"{name} {surname} ({nickname})"
        qr_img = self.generate_qr(qr_data)
        self.display_qr(qr_img)
        
        self.save_waiter(name, surname, nickname, qr_data)
        self.updateListView()




    def generate_qr(self, nickname):
        # Υποθέτουμε ότι το username είναι διαθέσιμο ως self.username στην κλάση
        url = f"http://{self.username}.localhost:8003/tables/table_selection/?nickname={nickname}"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img_byte_array = QByteArray()
        buffer = QBuffer(img_byte_array)
        buffer.open(QIODevice.WriteOnly)
        img.save(buffer, "PNG")
        pixmap = QPixmap()
        pixmap.loadFromData(img_byte_array)
        return pixmap



    def display_qr(self, img):
        img.save("waiter_qr.png")
        pixmap = QPixmap("waiter_qr.png")
        self.QrPlaceholder.setPixmap(pixmap)




    def save_waiter(self, name, surname, nickname, qr_data):
        conn = sqlite3.connect('waiters.db')
        c = conn.cursor()
        c.execute('INSERT INTO waiters (name, surname, nickname, qr_code) VALUES (?, ?, ?, ?)',
                  (name, surname, nickname, qr_data))
        conn.commit()
        conn.close()
        QMessageBox.information(self, "Success", "Waiter saved successfully!")


    def setup_qr_display(self):
        self.scroll_area = QScrollArea(self.QrPlaceholder)
        self.scroll_area.setWidgetResizable(True)
        # scroll_widget = QWidget()
        # self.grid_layout = QGridLayout(scroll_widget)
        # self.grid_layout.setSpacing(20)  # Αυξημένο διάστημα μεταξύ των widgets
        # self.grid_layout.setContentsMargins(20, 20, 20, 20)  # Αυξημένα περιθώρια
        # self.scroll_area.setWidget(scroll_widget)
        # self.scroll_area.setGeometry(10, 10, 731, 801)


    def create_frame(self, nickname, qr_pixmap):
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        frame.setStyleSheet("background-color: white; margin: 10px; padding: 10px; border-radius: 10px;")

        layout = QVBoxLayout(frame)
        label_nickname = QLabel(nickname)
        label_nickname.setAlignment(Qt.AlignCenter)

        label = QLabel()
        scaled_pixmap = qr_pixmap.scaled(250, 250, Qt.KeepAspectRatio, Qt.SmoothTransformation)  # Προσαρμογή μεγέθους QR
        label.setPixmap(scaled_pixmap)
        label.setFixedSize(250, 250)  # Περιορισμός μεγέθους QLabel

        layout.addWidget(label_nickname)
        layout.addWidget(label)

        return frame


if __name__ == "__main__":
    app = QApplication(sys.argv)
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        username = "default_username"

    main_window = MainWindow(username=username)
    main_window.show()
    sys.exit(app.exec())