# -*- coding: utf-8 -*-

import sys
import os
import json
from PySide6.QtWidgets import QApplication, QMainWindow
from reservation_ui import Ui_MainWindow
import sqlite3
from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsScene
from PySide6.QtGui import QColor, QFont
from PySide6.QtWidgets import QGraphicsTextItem
from PySide6.QtCore import Qt, QTime

class InteractiveTableItem(QGraphicsRectItem):
    def __init__(self, x, y, width, height, table_number, mainWindow):
        super().__init__(x, y, width, height)
        self.table_number = table_number
        self.mainWindow = mainWindow
        self.setBrush(QColor(0, 255, 0))
        self.setPen(QColor(0, 0, 0))
        self.setAcceptHoverEvents(True)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print(f"Τραπέζι {self.table_number} πατήθηκε.")
            self.mainWindow.fill_reservation_data(self.table_number)
            self.setBrush(QColor(255, 165, 0))  # Χρώμα κατά την επιλογή

    def hoverEnterEvent(self, event):
        self.setBrush(QColor(100, 255, 100))  # Ελαφρώς διαφορετικό χρώμα κατά το hover

    def hoverLeaveEvent(self, event):
        self.setBrush(QColor(0, 255, 0))  # Επιστροφή στο αρχικό χρώμα

class ReservationsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle("Reservations Window")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.bookingButton.clicked.connect(self.book_reservation)
        self.ui.calendarWidget.selectionChanged.connect(self.display_tables)
        self.ui.cancelReservationButton.clicked.connect(self.cancel_reservation)

        self.display_tables()
        self.initialize_database()

    @staticmethod
    def initialize_database():
        conn = sqlite3.connect('reserve.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reserve (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                table_number INTEGER NOT NULL,
                date TEXT NOT NULL,
                time TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def cancel_reservation(self):
        selected_date = self.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        table_number = self.ui.lineEdit_tableBook.text()

        if table_number:
            conn = sqlite3.connect('reserve.db')
            cursor = conn.cursor()

            cursor.execute('DELETE FROM reserve WHERE date = ? AND table_number = ?', (selected_date, table_number))
            conn.commit()
            conn.close()

            print(f"Κράτηση για τραπέζι {table_number} στις {selected_date} ακυρώθηκε.")
            self.display_tables()
            self.save_reservations_to_json()

    def book_reservation(self):
        name = self.ui.lineEdit_nameBook.text()
        phone = self.ui.lineEdit_phoneBook.text()
        table_number = self.ui.lineEdit_tableBook.text()
        time = self.ui.timeEdit_book.time().toString("HH:mm")
        date = self.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        if not (name and table_number and time and date):
            print("Τα πεδία ONOMA , ΤΡΑΠΕΖΙ είναι απαραίτητα.")
            return

        conn = sqlite3.connect('reserve.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO reserve (name, phone, table_number, date, time)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, phone, table_number, date, time))

        conn.commit()
        conn.close()

        print(f"Κράτηση: {date} {time} - Όνομα: {name}, Τηλέφωνο: {phone}, Τραπέζι: {table_number}")
        self.display_tables()
        self.save_reservations_to_json()

    def save_reservations_to_json(self):
        conn = sqlite3.connect('reserve.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM reserve')
        reservations = cursor.fetchall()
        conn.close()

        reservations_list = []
        for reservation in reservations:
            reservation_dict = {
                "id": reservation[0],
                "name": reservation[1],
                "phone": reservation[2],
                "table_number": reservation[3],
                "date": reservation[4],
                "time": reservation[5]
            }
            reservations_list.append(reservation_dict)

        if not os.path.exists('shared_data'):
            os.makedirs('shared_data')

        with open('shared_data/reservations.json', 'w', encoding='utf-8') as f:
            json.dump({"reservations": reservations_list}, f, ensure_ascii=False, indent=4)

    def display_tables(self):
        selected_date = self.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        conn = sqlite3.connect('reserve.db')
        cursor = conn.cursor()

        scene = QGraphicsScene(self)
        scene.clear()
        self.ui.graphicsView_reserve.setScene(scene)
        self.ui.graphicsView_reserve.setSceneRect(0, 0, 700, 300)

        text_color = QColor(0, 0, 0)

        try:
            with open('tables.txt', 'r') as file:
                tables_data = file.readlines()
        except FileNotFoundError:
            print("Το αρχείο tables.txt δεν βρέθηκε.")
            return

        num_tables = len(tables_data)
        rows = cols = int(num_tables ** 0.5) + 1  # Αύξηση των σειρών και στηλών για μεγαλύτερα τραπέζια
        margin = 20  # Αύξηση περιθωρίων
        width = (700 - (cols + 1) * margin) // cols  # Αύξηση πλάτους
        height = (300 - (rows + 1) * margin) // rows  # Αύξηση ύψους

        for i, line in enumerate(tables_data):
            row = i // cols
            col = i % cols
            x = col * (width + margin) + margin
            y = row * (height + margin) + margin

            table_color = QColor(0, 255, 0)

            cursor.execute('SELECT name, phone, time FROM reserve WHERE date = ? AND table_number = ?', (selected_date, i + 1))
            reservation = cursor.fetchone()

            if reservation:
                name, phone, time = reservation
                table_color = QColor(255, 0, 0)
                info_text = f"{name}\n{phone}\n{time}"
            else:
                info_text = str(i + 1)

            table_item = InteractiveTableItem(x, y, width, height, i + 1, self)
            table_item.setBrush(table_color)
            table_item.setPen(QColor(0, 0, 0))
            scene.addItem(table_item)

            text_item = QGraphicsTextItem(info_text, table_item)
            text_item.setDefaultTextColor(text_color)
            text_item.setFont(QFont("Segoe UI", 12))  # Αύξηση μεγέθους γραμματοσειράς
            text_item.setPos(x + width / 2 - text_item.boundingRect().width() / 2,
                             y + height / 2 - text_item.boundingRect().height() / 2)
            scene.addItem(text_item)

        conn.close()
        self.ui.graphicsView_reserve.show()

    def fill_reservation_data(self, table_number):
        selected_date = self.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        conn = sqlite3.connect('reserve.db')
        cursor = conn.cursor()

        cursor.execute('SELECT name, phone, time FROM reserve WHERE date = ? AND table_number = ?', (selected_date, table_number))
        reservation = cursor.fetchone()

        if reservation:
            name, phone, time = reservation
            self.ui.lineEdit_nameBook.setText(name)
            self.ui.lineEdit_phoneBook.setText(phone)
            self.ui.lineEdit_tableBook.setText(str(table_number))
            self.ui.timeEdit_book.setTime(QTime.fromString(time, "HH:mm"))
        else:
            self.ui.lineEdit_nameBook.clear()
            self.ui.lineEdit_phoneBook.clear()
            self.ui.lineEdit_tableBook.setText(str(table_number))
            self.ui.timeEdit_book.clear()

        conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    reservations_window = ReservationsWindow()
    reservations_window.show()
    sys.exit(app.exec())
