import sys
import cv2
import json
import os
import sqlite3
import cv2
import datetime
import logging
import math
import numpy as np
import pyqtgraph as pg
import requests
import shutil
import subprocess
import threading
import time
from datetime import datetime, timedelta
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.dates as mdates
from matplotlib.ticker import MaxNLocator
from model_functions import run_models, identify_tables
from PySide6.QtCore import QDateTime, Qt, QTimer, QDate, QUrl, QProcess
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QFileDialog,
                               QGraphicsScene, QMessageBox,
                               QTableWidgetItem, QGraphicsPixmapItem,
                               QGraphicsRectItem, QGraphicsTextItem,
                               QGridLayout, QStyledItemDelegate, QAbstractItemView, QVBoxLayout, QLabel)

import database_manager as database_manager
from reservations import ReservationsWindow
import matplotlib.pyplot as plt
import j as j
from PySide6.QtCore import QUrl, QTimer
from interface_ui import Ui_MainWindow
from PySide6.QtGui import QPixmap, QFont, QStandardItemModel, QStandardItem, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QGridLayout, QGraphicsScene, QTableWidgetItem, QMessageBox
from PySide6.QtWidgets import QScrollArea, QWidget, QVBoxLayout, QPushButton, QLabel, QGridLayout
import colorsys
from PySide6.QtWidgets import QFrame, QHBoxLayout, QPushButton, QGraphicsScene, QTableWidgetItem, QVBoxLayout
from PySide6.QtCore import QDate, QDateTime, Qt, QTimer, QRect
from PySide6.QtGui import QPixmap, QColor, QFont

database_manager.initialize_db_tables_occupation()




logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Λήψη της διαδρομής του τρέχοντος αρχείου
if getattr(sys, 'frozen', False):
    # Τρέχει από το εκτελέσιμο που δημιουργήθηκε με το PyInstaller
    current_dir = os.path.dirname(sys.executable)
else:
    # Τρέχει από το Python script
    current_dir = os.path.dirname(os.path.abspath(__file__))

# Καθορισμός της διαδρομής των αρχείων
data_file_path = os.path.join(current_dir, 'shared_data', 'occupied_tables.json')
tables_file_path = os.path.join(current_dir, 'tables.txt')

logger.debug(f"Current directory: {current_dir}")
logger.debug(f"Data file path: {data_file_path}")
logger.debug(f"Tables file path: {tables_file_path}")

# Έλεγχος αν τα αρχεία υπάρχουν
if not os.path.exists(data_file_path):
    logger.error(f"File not found: {data_file_path}")
    logger.debug(f"Contents of current directory: {os.listdir(current_dir)}")
    sys.exit(f"File not found: {data_file_path}")

if not os.path.exists(tables_file_path):
    logger.error(f"File not found: {tables_file_path}")
    logger.debug(f"Contents of current directory: {os.listdir(current_dir)}")
    sys.exit(f"File not found: {tables_file_path}")

# Διαβάστε το αρχείο occupied_tables.json
try:
    with open(data_file_path, 'r') as file:
        data = json.load(file)
    logger.debug(f"Data loaded: {data}")
except FileNotFoundError:
    logger.error(f"File not found: {data_file_path}")
    sys.exit(f"File not found: {data_file_path}")

# Διαβάστε το αρχείο tables.txt
try:
    with open(tables_file_path, 'r') as file:
        tables = file.read()
    logger.debug(f"Tables data loaded: {tables}")
except FileNotFoundError:
    logger.error(f"File not found: {tables_file_path}")
    sys.exit(f"File not found: {tables_file_path}")













class TimeDiffDelegate(QStyledItemDelegate):
    def displayText(self, value, locale):
        timestamp = QDateTime.fromString(value, "yyyy-MM-dd HH:mm:ss")
        if not timestamp.isValid():
            return "Μη έγκυρος χρόνος"
        time_diff = QDateTime.currentDateTime().secsTo(timestamp)
        hours = abs(time_diff) // 3600
        minutes = (abs(time_diff) % 3600) // 60
        return f"{hours:02}:{minutes:02} HH:MM"

class CenterAlignDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        option.displayAlignment = Qt.AlignCenter
        super(CenterAlignDelegate, self).paint(painter, option, index)

def initialize_db():
    logger.debug("init db")
    try:
        with sqlite3.connect('products.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category TEXT,
                    description TEXT,
                    price REAL,
                    amount INTEGER
                )
            ''')
            conn.commit()
    except sqlite3.Error as e:
        print(f"Σφάλμα κατά την αρχικοποίηση του πίνακα products: {e}")

def add_record(category, description, price, amount):
    try:
        with sqlite3.connect('products.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO products (category, description, price, amount) VALUES (?, ?, ?, ?)',
                           (category, description, price, amount))
            conn.commit()
            print("Εισαγωγή επιτυχής")
    except sqlite3.Error as e:
        print(f"Σφάλμα κατά την εισαγωγή: {e}")

def search_database(field, text):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    if field not in ['category', 'description', 'price', 'amount']:
        raise ValueError("Invalid field name")
    query = f"SELECT * FROM products WHERE {field} LIKE ?"
    cursor.execute(query, ('%' + text + '%',))
    results = cursor.fetchall()
    conn.close()
    return results

def delete_record(record_id):
    try:
        with sqlite3.connect('example.db') as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM products WHERE id = ?', (record_id,))
            conn.commit()
            print("Διαγραφή επιτυχής")
    except sqlite3.Error as e:
        print("Σφάλμα κατά τη διαγραφή:", e)

def delete_local_received_orders_files(table_number, local_directory='received_orders'):
    try:
        for filename in os.listdir(local_directory):
            if f"table_{table_number}_" in filename:
                os.remove(os.path.join(local_directory, filename))
                print(f"Διαγράφηκε τοπικά το αρχείο: {filename}")
    except Exception as e:
        print(f"Σφάλμα κατά τη διαγραφή τοπικών αρχείων: {e}")

class MainWindow(QMainWindow, Ui_MainWindow):
    logger.debug("Starting the z.py script")
    def __init__(self, parent=None, username="default_username"):

        super(MainWindow, self).__init__(parent)
        self.username = username
        self.setupUi(self)

        self.parameters_file = "parameters.json"  # Αρχικοποίηση της parameters_file

        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(self.run_tasks)
        self.timer1.start(8003)

        self.timer2 = QTimer(self)
        self.timer2.timeout.connect(self.run_tasks2)
        self.timer2.start(15000)

        self.init_tables_2.clicked.connect(self.execute_identify_tables)
        self.run_model_button.clicked.connect(self.execute_model)
        self.toolButton_choose_image.clicked.connect(self.load_image)

        self.graphicsScene = QGraphicsScene(self)
        self.graphicsView.setScene(self.graphicsScene)
        self.initial_image_path = 'tables_init.jpg'
        if os.path.exists(self.initial_image_path):
            self.update_image(self.initial_image_path)
        self.load_parameters()

        self.iou_spin_box.valueChanged.connect(self.save_parameters)
        self.conf_spin_box.valueChanged.connect(self.save_parameters)
        self.annonate_image.clicked.connect(self.start_annotations)
        self.annotations = []
        self.drawing = False
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.execute_timer)

        self.timer_spinBox.valueChanged.connect(self.update_timer)
        self.timer_spinBox.valueChanged.connect(self.save_parameters)
        self.update_timer()

        self.green_led_icon = QPixmap("icons/green.png")
        self.red_led_icon = QPixmap("icons/red.png")
        self.update_led("red")
        self.update_tables_view()
        self.reset_occupation_time.clicked.connect(self.confirm_reset)
        self.notify_limit = 5
        self.spinBox_notify_minutes.setValue(self.notify_limit)
        self.spinBox_notify_minutes.valueChanged.connect(self.set_notify_limit_value)
        self.spinBox_notify_minutes.valueChanged.connect(self.save_parameters)
        self.update_tables_view()
        self.load_parameters()
        # self.reset_hour_data.clicked.connect(self.reset_database_data)
        # self.daily_timer = QTimer(self)
        # self.daily_timer.timeout.connect(self.check_for_new_day)
        # self.daily_timer.start(86400000)
        self.last_checked_date = QDate.currentDate()
        self.live_update_timer = QTimer(self)
        self.live_update_timer.start(60000)
        self.scene = QGraphicsScene(self)
        self.initialize_tables()
        self.view_width = 700
        self.view_height = 500
        self.tables_placement = self.read_table_data()
        self.pushButton_submit_item.clicked.connect(self.onSubmit)
        self.productListView.clicked.connect(self.onListItemClicked)
        self.lineEdit_category.returnPressed.connect(self.onSubmit)
        self.lineEdit_description.returnPressed.connect(self.onSubmit)
        self.lineEdit_price.returnPressed.connect(self.onSubmit)
        self.lineEdit_amount.returnPressed.connect(self.onSubmit)

        self.model_category = QStandardItemModel(self)
        self.listView_category.setModel(self.model_category)

        self.model_description = QStandardItemModel(self)
        self.listView_description.setModel(self.model_description)

        self.lineEdit_category.textChanged.connect(self.onCategoryTextChanged)
        self.lineEdit_description.textChanged.connect(self.onDescriptionTextChanged)

        self.listView_category.clicked.connect(self.onListViewCategoryClicked)
        self.listView_description.clicked.connect(self.onListViewDescriptionClicked)
        self.productListModel = QStandardItemModel(self)
        self.productListView.setModel(self.productListModel)

        self.setup_database()
        self.timeDiffDelegate = TimeDiffDelegate(self.tableView)
        self.tableView.setItemDelegateForColumn(4, self.timeDiffDelegate)

        self.gridLayout_button = QGridLayout()

        self.pushButton_to_reservations.clicked.connect(self.open_reservations)
        self.open_windows = {}
        username = sys.argv[1] if len(sys.argv) > 1 else 'default_username'
        self.webEngineView.setUrl(QUrl(f"http://{username}.localhost:8003/table_selection/"))
        self.webEngineView_2.setUrl(QUrl(f"http://{username}.localhost:8003/order_summary/"))
        self.webEngineView_3.setUrl(QUrl(f"http://{username}.localhost:8003/table_selection_with_time_diff/"))
        # Εκτέλεση JavaScript μετά τη φόρτωση των σελίδων για αλλαγή του background color
        self.webEngineView.loadFinished.connect(lambda: self.change_background_color(self.webEngineView))
        self.webEngineView_2.loadFinished.connect(lambda: self.change_background_color(self.webEngineView_2))
        self.webEngineView_3.loadFinished.connect(lambda: self.change_background_color(self.webEngineView_3))

        self.last_active_table = None
        self.active_table_number = None
        self.last_active_table = None
        self.gridLayout_button = QGridLayout()
        self.frame_23.setLayout(self.gridLayout_button)
        self.initialize_buttons()
        self.pushButton_printOrder.clicked.connect(self.print_order)
        self.pushButton_deleteOrder.clicked.connect(self.delete_order)
        self.create_old_orders_table()
        self.selected_table_number = None
        self.tableWidget_ord.setHorizontalHeaderLabels(['ID', 'Περιγραφή', 'Ποσότητα', 'Κόστος'])
        self.pushButton_delete_item.clicked.connect(self.delete_selected_item)
        self.productListView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.pushButton_camera_live.clicked.connect(self.start_camera_stream)
        self.pushButton_waiters.clicked.connect(self.show_waiters)
        self.update_labels()

        self.setStyleSheet("""
            QMessageBox {
                background-color: #f0f0f0;
                font: bold 12px;
            }
            QPushButton {
                background-color: #e7e7e7;
                border-radius: 10px;
                font:  15px;
                padding: 5px;
            }
            QProgressDialog {
                background-color: lightgray;
            }
            QProgressBar {
                
                border-radius: 1px;
                text-align: center;
                
            }
            QProgressBar::chunk {
                background-color: #05B8CC;
                width: 20px;
            }
        """)

    def change_background_color(self, web_engine_view):
        script = """
        document.body.style.backgroundColor = 'rgb(208, 212, 217)';
        document.body.style.color = 'white';
        """
        web_engine_view.page().runJavaScript(script)
        

    def update_tables_view(self):
        if not os.path.exists('shared_data/occupied_tables.json'):
            with open('shared_data/occupied_tables.json', 'w') as file:
                json.dump({'tables': []}, file)

        with open('shared_data/occupied_tables.json', 'r') as file:
            data = json.load(file)

        self.tableView.setColumnCount(2)
        self.tableView.setHorizontalHeaderLabels(["#", "Occupied Time"])
        self.tableView.horizontalHeader().setVisible(True)
        self.tableView.verticalHeader().setVisible(False)

        self.tableView.clearContents()
        self.tableView.setRowCount(0)
        # Ρύθμιση του style sheet για τις οριζόντιες και κάθετες επικεφαλίδες
        header_style = "QHeaderView::section { background-color: gray; color: white; }"
        self.tableView.horizontalHeader().setStyleSheet(header_style)
        self.tableView.verticalHeader().setStyleSheet(header_style)
        # Ορίζετε το πλάτος των στηλών
        self.tableView.setColumnWidth(0, 30)  # Για την στήλη "#"
        self.tableView.setColumnWidth(1, 100)  # Για την στήλη "Occupied"

        current_status = self.get_current_status()  # Λίστα των αριθμών τραπεζιών με order_done = 1

        for table in data["tables"]:
            table_number = table["table_number"]
            duration = table.get("duration", "")

            row = self.find_row_by_table_number(table_number)
            if row is None:
                self.tableView.insertRow(self.tableView.rowCount())
                row = self.tableView.rowCount() - 1

            duration_minutes = self.convert_duration(duration)
            notify_limit = self.spinBox_notify_minutes.value()

            table_number_item = QTableWidgetItem(str(table_number))
            table_number_item.setBackground(QColor("#333333"))
            table_number_item.setForeground(QColor("white"))

            duration_hm = ":".join(duration.split(":")[:2])
            duration_item = QTableWidgetItem(duration_hm)
            duration_item.setForeground(QColor("white"))
            delivered_item = QTableWidgetItem()

            if table_number in current_status:
                duration_item.setBackground(QColor("Green"))
            else:
                if duration_minutes > notify_limit:
                    duration_item.setBackground(QColor("red"))

            self.tableView.setItem(row, 0, table_number_item)
            self.tableView.setItem(row, 1, duration_item)
            self.tableView.setItem(row, 2, delivered_item)

        self.tableView.setSortingEnabled(True)
        self.tableView.sortItems(1, Qt.DescendingOrder)


    def format_duration_to_HHMM(self, duration_minutes):
        hours = duration_minutes // 60
        minutes = duration_minutes % 60
        return f"{hours:02d}:{minutes:02d}"




    def fetch_order_status(self, db_path):
        orders_status = {}
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT table_number, COUNT(*) as total_orders, 
                    SUM(CASE WHEN order_done = 1 THEN 1 ELSE 0 END) as orders_done
                FROM orders
                GROUP BY table_number
            """)
            for row in cursor.fetchall():
                table_number, total_orders, orders_done = row
                orders_status[table_number] = {
                    'total_orders': total_orders,
                    'orders_done': orders_done,
                    'orders_not_done': total_orders - orders_done
                }
        return orders_status

    def update_labels(self):
        tables = self.read_tables_file('tables.txt')
        latest_records = self.fetch_latest_records('tables_occupation.db', tables)
        orders_status = self.fetch_order_status('example.db')

        total_tables = len(latest_records)
        occupied_tables = sum(1 for record in latest_records.values() if self.convert_duration_to_seconds(record[3]) > 0)
        free_tables = total_tables - occupied_tables

        self.label_number_of_tables.setText(str(total_tables))
        self.label_occupied_tables.setText(str(occupied_tables))
        self.label_free_tables.setText(str(free_tables))

    def convert_duration_to_seconds(self, duration):
        days, time_part = 0, duration
        if 'day' in duration or 'days' in duration:
            parts = duration.split(',')
            days = int(parts[0].split()[0])
            time_part = parts[1].strip()

        time_parts = time_part.split(':')
        hours, minutes, seconds = 0, 0, 0
        if len(time_parts) == 3:
            hours, minutes, seconds = map(int, time_parts)
        elif len(time_parts) == 2:
            hours, minutes = map(int, time_parts)

        total_seconds = days * 86400 + hours * 3600 + minutes * 60 + seconds
        return total_seconds

    def read_tables_file(self, file_path):
        tables = {}
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 5:
                    id = int(parts[0])
                    tables[id] = parts
        return tables

    def fetch_latest_records(self, db_path, tables):
        latest_records = {}
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            for table_id in tables.keys():
                cursor.execute("""
                    SELECT * FROM tables
                    WHERE table_id = ?
                    ORDER BY record_time DESC
                    LIMIT 1
                """, (table_id,))
                record = cursor.fetchone()
                if record:
                    latest_records[table_id] = record
        return latest_records

    def start_annotations(self):
        self.process = QProcess(self)
        script_path = os.path.join(os.path.dirname(__file__), 'annotation.py')
        self.process.start("python", [script_path])

    def start_camera_stream(self):
        # Εδώ θα πρέπει να καλέσετε την κάμερα ή να εκτελέσετε το camera_stream.py
        # Παράδειγμα: Εκκίνηση ενός εξωτερικού script
        print("Κάμερα")
        self.process = QProcess(self)
        script_path = os.path.join(os.path.dirname(__file__), 'camera_stream.py')
        self.process.start("python", [script_path])

    def show_waiters(self):
        # Εδώ θα πρέπει να καλέσετε την κάμερα ή να εκτελέσετε το camera_stream.py
        # Παράδειγμα: Εκκίνηση ενός εξωτερικού script
        self.process = QProcess(self)
        script_path = os.path.join(os.path.dirname(__file__), 'waiters.py')
        self.process.start("python", [script_path])

    def execute_model(self):
        if self.image_path is None:
            QMessageBox.warning(self, "Προσοχή", "Επιλέξτε πρώτα εικόνα")
            return

        iou = self.iou_spin_box.value()
        conf = self.conf_spin_box.value()
        # run_models(self.image_path, iou, conf)
        # Δημιουργία και εκκίνηση ενός νέου νήματος για την εκτέλεση της run_models
        thread = threading.Thread(target=run_models, args=(self.image_path, iou, conf))
        thread.start()

        print("Παράμετροι:")
        print(iou, conf)
        print("Εικόνα:")
        print(self.image_path)

        self.initialize_tables()
        self.update_data()
  
   
        self.tables_placement = self.read_table_data()
        self.add_tables_to_scene(self.tables_placement, self.image_width, self.image_height)

    def execute_timer(self):
        self.update_led("red")

        # Εκτέλεση της συνάρτησης execute_model αν υπάρχει έγκυρο μονοπάτι εικόνας
        if self.image_path:
            self.execute_model()
            self.update_led("green")

        # Συνέχεια με τις υπόλοιπες ενημερώσεις του UI
        self.update_image('tables_visualization.jpg')
        self.update_tables_view()
        self.update_data()
        self.tables_placement = self.read_table_data()
        self.add_tables_to_scene(self.tables_placement, self.image_width, self.image_height)

    def run_tasks(self):
        j.process_all_json_files('received_orders')
        self.setup_database()
        self.update_tables_view()
        self.update_selected_table_orders()
        self.update_buttons()  # Προσθήκη της κλήσης για ενημέρωση της αναφοράς
        self.update_labels()

    def run_tasks2(self):
        pass

    def execute_identify_tables(self):
        if self.image_path is None:
            QMessageBox.warning(self, "Προσοχή", "Επιλέξτε πρώτα εικόνα")
            return

        iou, conf = self.load_parameters() # type: ignore
        identify_tables(self.image_path, iou, conf)
        
        # Καθορισμός της διαδρομής της αρχικής και της νέας εικόνας
        destination_image_path = 'tables_init.jpg'
        self.update_image(destination_image_path)  # Ενημέρωση της εικόνας στο UI

    def confirm_save(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setWindowTitle("Επιβεβαίωση Αποθήκευσης")
        msgBox.setText("Θέλετε να προσθέσετε τα νέα πλαίσια στα υπάρχοντα ή να αντικαταστήσετε το αρχείο;")
        addButton = msgBox.addButton("Προσθήκη", QMessageBox.YesRole)
        replaceButton = msgBox.addButton("Αντικατάσταση", QMessageBox.NoRole)
        cancelButton = msgBox.addButton("Ακύρωση", QMessageBox.RejectRole)
        msgBox.setDefaultButton(cancelButton)

        response = msgBox.exec()

        if response == 0:  # Προσθήκη
            return "add"
        elif response == 1:  # Αντικατάσταση
            return "replace"
        else:  # Ακύρωση
            return "cancel"
        
    def load_parameters(self):
        default_params = {
            'iou': 0.07,
            'conf': 0.07,
            'timer_interval': 2,
            'notify_limit': 5
        }

        try:
            if os.path.exists(self.parameters_file):
                with open(self.parameters_file, 'r') as file:
                    params = json.load(file)
            else:
                params = default_params
                with open(self.parameters_file, 'w') as file:
                    json.dump(params, file, indent=4)

            self.iou_spin_box.setValue(params.get('iou', 0.07))
            self.conf_spin_box.setValue(params.get('conf', 0.07))
            self.timer_spinBox.setValue(params.get('timer_interval', 2))
            self.spinBox_notify_minutes.setValue(params.get('notify_limit', 5))
        except json.JSONDecodeError:
            print("Σφάλμα κατά τη φόρτωση του αρχείου JSON. Χρησιμοποιούνται οι προεπιλεγμένες τιμές.")
            with open(self.parameters_file, 'w') as file:
                json.dump(default_params, file, indent=4)

            self.iou_spin_box.setValue(default_params['iou'])
            self.conf_spin_box.setValue(default_params['conf'])
            self.timer_spinBox.setValue(default_params['timer_interval'])
            self.spinBox_notify_minutes.setValue(default_params['notify_limit'])

    def save_parameters(self):
        params = {
            'iou': self.iou_spin_box.value(),
            'conf': self.conf_spin_box.value(),
            'timer_interval': self.timer_spinBox.value(),
            'notify_limit': self.spinBox_notify_minutes.value()  # Χρήση της τιμής από το spinBox_notify_minutes
        }
        with open(self.parameters_file, 'w') as file:
            json.dump(params, file, indent=4)

        # Σύνδεση του spinBox_notify_minutes με την save_parameters
        self.spinBox_notify_minutes.valueChanged.connect(self.save_parameters)

    def confirm_reset(self):
        # Παράθυρο διαλόγου για επιβεβαίωση
        reply = QMessageBox.question(self, 'Επιβεβαίωση', 'Θέλετε να επαναφέρετε τα δεδομένα κατάληψης;',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.reset_occupation_data()

    def reset_occupation_data(self):
        # Διαγραφή δεδομένων από το αρχείο shared_data/occupied_tables.json
        data = {'tables': []}
        with open('occupied_since.json', 'w') as file:
            json.dump(data, file, indent=4)

        # Ενημέρωση της εμφάνισης
        self.execute_model()
        self.update_tables_view()



    def open_reservations(self):
        reservations_window = ReservationsWindow()
        reservations_window.show()
        self.open_windows[reservations_window] = reservations_window

    def create_old_orders_table(self):
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS old_orders (
                id                  INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id            INTEGER UNIQUE,
                table_number        INTEGER,
                product_description TEXT,
                quantity            INTEGER,
                total_cost          REAL,
                time_diff           TEXT,
                waiter              TEXT,
                order_done          BOOLEAN,
                printed             BOOLEAN,
                timestamp           TEXT
                );
        ''')
        conn.commit()
        conn.close()

    def delete_received_orders_files(self, table_number):
        url = 'http://localhost:8003//delete_received_orders/'
        data = {'table_number': table_number}
        response = requests.post(url, json=data)

        if response.status_code == 200:
            print("Τα αρχεία διαγράφηκαν επιτυχώς από το Django server.")
            delete_local_received_orders_files(self.active_table_number, 'received_orders')
        else:
            print("Πρόβλημα κατά τη διαγραφή αρχείων.")
        print(f"Κωδικός απόκρισης: {response.status_code}")

    def update_selected_table_orders(self):
        if self.selected_table_number is not None:
            self.show_table_orders(self.selected_table_number)
            print('-----   Η λιστα ενημερωθηκε  -------------')

    def show_table_orders(self, table_number):
        if table_number is None:
            print("Δεν έχει δοθεί έγκυρος αριθμός τραπεζιού")
            self.delete_orders_for_table(table_number)
            return

        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()

        # Ανάκτηση των παραγγελιών για το συγκεκριμένο τραπέζι
        query = """
            SELECT product_description, quantity, total_cost 
            FROM orders 
            WHERE table_number = ? AND order_done = 1 AND printed = 0
        """
        cursor.execute(query, (table_number,))
        records = cursor.fetchall()
        conn.close()

        # Διαμόρφωση του QTableWidget
        self.tableWidget_ord.setRowCount(0)
        self.tableWidget_ord.setColumnCount(3)
        self.tableWidget_ord.setHorizontalHeaderLabels(['Product', 'Quant.', 'Cost'])

        # Ρύθμιση των μηκών των κελιών
        self.tableWidget_ord.setColumnWidth(0, 280)
        self.tableWidget_ord.setColumnWidth(1, 60)
        self.tableWidget_ord.setColumnWidth(2, 80)

        for row_number, row_data in enumerate(records):
            self.tableWidget_ord.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.tableWidget_ord.setItem(row_number, column_number, item)

        # Υπολογισμός του συνολικού κόστους
        grand_total = sum(row[2] for row in records)

        # Ενημέρωση του QLabel για την εμφάνιση του αριθμού του τραπεζιού και του συνολικού κόστους
        self.label_table_feat.setText(f"Table: {table_number} - Grand Total: {grand_total:.2f}")

        self.tableWidget_ord.setStyleSheet("""
        QTableWidget {
            color: rgb(31, 90, 94);  /* Χρώμα γραμμάτων των κελιών */
            gridline-color: rgb(118, 118, 118);  /* Χρώμα των γραμμών του πλέγματος */
            selection-background-color: gray;  /* Χρώμα φόντου για επιλεγμένα κελιά */
        }
        QHeaderView::section {
            background-color: rgb(128, 128, 128);  /* Χρώμα φόντου για τα headers των στηλών και των γραμμών */
            color: rgb(0, 100, 0);  /* Χρώμα γραμμάτων για τα headers των στηλών και των γραμμών, 'dark green' σε RGB */
        }
        """)

    def delete_orders_for_table(self, table_number):
        if table_number is None:
            return

        try:
            conn = sqlite3.connect('example.db')
            cursor = conn.cursor()

            # Διαγραφή των παραγγελιών για το συγκεκριμένο τραπέζι
            delete_query = """
                DELETE FROM orders 
                WHERE table_number = ? 
            """
            cursor.execute(delete_query, (table_number,))
            conn.commit()
            conn.close()
            print(f"Οι παραγγελίες για το τραπέζι {table_number} διαγράφηκαν επιτυχώς.")
        except sqlite3.Error as e:
            print(f"Σφάλμα κατά τη διαγραφή των παραγγελιών για το τραπέζι {table_number}: {e}")

    #  Διαβασμα της βασης δεδομενων για τις παραγγελιες στο tab orders
    def setup_database(self):
        # Ελέγχουμε αν η σύνδεση με τη βάση δεδομένων υπάρχει ήδη
        if QSqlDatabase.contains("qt_sql_default_connection"):
            self.database = QSqlDatabase.database("qt_sql_default_connection")
        else:
            self.database = QSqlDatabase.addDatabase("QSQLITE")
            self.database.setDatabaseName("example.db")

        # Άνοιγμα της βάσης δεδομένων
        if not self.database.open():
            print("Σφάλμα στη σύνδεση με τη βάση δεδομένων")
            return

        # Δημιουργία του μοντέλου
        self.model = QSqlTableModel(self, self.database)
        self.model.setTable("orders")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)

        # Ορισμός φίλτρου
        self.model.setFilter("order_done = 0")
        self.model.select()

    #  ΕΚΤΥΠΩΣΗ ΚΑΤΧΩΡΗΣΗ ΣΤΗ ΒΑΣΗ ΚΑΙ ΔΙΑΓΡΑΦΗ JSON 
    def print_order(self):
        if self.active_table_number is None:
            print("Δεν έχει επιλεγεί καμία παραγγελία για εκτύπωση.")
            QMessageBox.information(self, "Προειδοποίηση", "Δεν έχει επιλεγεί καμία παραγγελία για εκτύπωση.")
            return
        
        if self.check_unprepared_orders(self.active_table_number):
            QMessageBox.information(self, 'Ανεκτέλεστη Παραγγελία', 
                                    'Η παραγγελία δεν έχει ετοιμαστεί και δεν μπορεί να εκτυπωθεί. Εάν θέλετε, μπορείτε να την διαγράψετε με το κουμπι "Delete Order".')
            return
        
        # Εμφάνιση μηνύματος επιβεβαίωσης
        reply = QMessageBox.question(self, 'Επιβεβαίωση Εκτύπωσης', 
                                    'Είστε σίγουροι ότι θέλετε να εκτυπώσετε την παραγγελία;',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            self.process_and_delete_orders(self.active_table_number, self.username)
            
            order_text, additional_info = self.get_order_details(self.active_table_number)
            self.create_rtf_order(order_text, additional_info)
        else:
            print("Η εκτύπωση ακυρώθηκε από τον χρήστη.")

    def get_order_details(self, table_number):
        order_text = ""
        additional_info = {
            'store_name': 'Το Κατάστημα Μου',
            'date': datetime.now().strftime('%Y-%m-%d'),
            'time': datetime.now().strftime('%H:%M:%S'),
            'total_cost': 0.0,
            'taxes': 0.0
        }

        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT product_description, quantity, total_cost 
            FROM orders 
            WHERE table_number = ? AND order_done = 1 AND printed = 0
        """, (table_number,))
        records = cursor.fetchall()
        conn.close()

        total_cost = 0.0
        for row in records:
            product_description, quantity, cost = row
            order_text += f"{product_description} - {quantity} - {cost}\n"
            total_cost += cost

        additional_info['total_cost'] = total_cost
        additional_info['taxes'] = total_cost * 0.24  # Παράδειγμα υπολογισμού φόρου 24%

        return order_text, additional_info

    def create_rtf_order(self, order_text, additional_info):
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"order_table{self.active_table_number}_{timestamp}.rtf"
            directory = "old_orders"

            if not os.path.exists(directory):
                os.makedirs(directory)

            file_path = os.path.join(directory, filename)
            
            rtf_content = self.construct_rtf_content(order_text, additional_info)
            
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(rtf_content)
            
            print(f"Το αρχείο RTF δημιουργήθηκε επιτυχώς: {file_path}")
        
        except Exception as e:
            print(f"Σφάλμα κατά τη δημιουργία του αρχείου RTF: {e}")

    def construct_rtf_content(self, order_text, additional_info):
        rtf_header = r'{\rtf1\ansi\ansicpg1253\uc1\deff0{\fonttbl{\f0\fnil\fcharset0 Arial;}}'
        rtf_footer = r'}'

        rtf_content = f"\\b Κατάστημα: {additional_info['store_name']}\\b0\\line\n"
        rtf_content += f"Ημερομηνία: {additional_info['date']}\\line\n"
        rtf_content += f"Ώρα: {additional_info['time']}\\line\n"
        rtf_content += "\\line\n"

        rtf_content += order_text.replace('\n', '\\line\n') + '\\line\n'

        rtf_content += f"Συνολικό Κόστος: {additional_info['total_cost']}\\line\n"
        rtf_content += f"Φόροι: {additional_info['taxes']}\\line\n"

        return rtf_header + rtf_content + rtf_footer

    def check_unprepared_orders(self, table_number):
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()
        try:
            cursor.execute('''
                SELECT COUNT(*) FROM orders
                WHERE table_number = ? AND order_done = 0 AND printed = 0
            ''', (table_number,))
            count = cursor.fetchone()[0]
            return count > 0
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False
        finally:
            conn.close()

    def process_and_delete_orders(self, table_number, username):
        db_path = 'example.db'
        local_folder_path = 'received_orders'
        delete_url = f'http://{username}.localhost:8003/delete_received_orders/{username}/'

        try:
            # Σύνδεση με τη Βάση Δεδομένων
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # Ερώτημα στη Βάση Δεδομένωνf
            cursor.execute('''
                SELECT order_id FROM orders
                WHERE table_number = ? AND order_done=1 AND printed=0
            ''', (table_number,))
            orders = cursor.fetchall()

            order_ids = [order[0] for order in orders]
            data = {'order_ids': order_ids}
            
            # Αποστολή Δεδομένων για Διαγραφή
            response = requests.delete(delete_url, json=data)
            if response.status_code == 200:
                print("Response from server:", response.json())

                # Διαγραφή και αντιγραφή εγγραφών στον πίνακα old_orders
                cursor.executemany('INSERT INTO old_orders SELECT * FROM orders WHERE order_id = ?', [(id,) for id in order_ids])
                cursor.executemany('DELETE FROM orders WHERE order_id = ?', [(id,) for id in order_ids])
                conn.commit()

                # Διαγραφή όλων των JSON αρχείων στο φάκελο received_orders
                for file in os.listdir(local_folder_path):
                    os.remove(os.path.join(local_folder_path, file))
                    print(f"Deleted local file: {file}")

                # Διαγραφή εγγραφών από τον πίνακα orders για orders με order_done = 0 και printed = 0
                cursor.execute('''
                    DELETE FROM orders
                    WHERE table_number = ? AND order_done = 0 AND printed = 0
                ''', (table_number,))
                conn.commit()
                print(f"Οι παραγγελίες για το τραπέζι {table_number} με order_done = 0 και printed = 0 διαγράφηκαν από τη βάση δεδομένων.")

            else:
                print("Failed to delete files from server, Status code:", response.status_code)
                if response.text:
                    print("Response message:", response.text)

        except sqlite3.Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"General error: {e}")
        finally:
            # Κλείσιμο Σύνδεσης
            conn.close()

    def delete_order(self):
        if self.active_table_number is None:
            print("Δεν έχει επιλεγεί καμία παραγγελία για διαγραφή.")
            return

        # Εμφάνιση προειδοποιητικού μηνύματος
        reply = QMessageBox.question(self, 'Επιβεβαίωση Διαγραφής', 
                                    'Είστε σίγουροι ότι θέλετε να διαγράψετε την παραγγελία από το τραπέζι {}?'.format(self.active_table_number),
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.delete_order_from_database(self.active_table_number)
            self.active_table_number = None  # Επαναφέρετε την τιμή μετά τη διαγραφή
            self.show_table_orders(self.active_table_number)
        else:
            print("Η διαγραφή ακυρώθηκε.")

    def delete_order_from_database(self, table_number):
        if table_number is None or not isinstance(table_number, int):
            print("Δεν έχει δοθεί έγκυρος αριθμός τραπεζιού.")
            return

        db_path = 'example.db'
        local_folder_path = 'received_orders'
        delete_url = f'http://{self.username}.localhost:8003/delete_received_orders/{self.username}/'

        try:
            # Σύνδεση με τη Βάση Δεδομένων
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # Ερώτημα στη Βάση Δεδομένων για όλες τις παραγγελίες του συγκεκριμένου τραπεζιού
            cursor.execute('''
                SELECT order_id FROM orders
                WHERE table_number = ?
            ''', (table_number,))
            orders = cursor.fetchall()

            order_ids = [order[0] for order in orders]
            data = {'order_ids': order_ids}

            # Αποστολή Δεδομένων για Διαγραφή
            response = requests.delete(delete_url, json=data)
            if response.status_code == 200:
                print("Response from server:", response.json())

                # Διαγραφή όλων των JSON αρχείων στο φάκελο received_orders
                for file in os.listdir(local_folder_path):
                    os.remove(os.path.join(local_folder_path, file))
                    print(f"Deleted local file: {file}")

                # Διαγραφή εγγραφών από τον πίνακα orders για orders με order_done = 0 και printed = 0
                cursor.execute('''
                    DELETE FROM orders
                    WHERE table_number = ? 
                ''', (table_number,))
                conn.commit()
                print(f"Οι παραγγελίες για το τραπέζι {table_number}  διαγράφηκαν από τη βάση δεδομένων.")

            else:
                print("Failed to delete files from server, Status code:", response.status_code)
                if response.text:
                    print("Response message:", response.text)

        except sqlite3.Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"General error: {e}")
        finally:
            # Κλείσιμο Σύνδεσης
            conn.close()

        # Ανανέωση του πίνακα
        self.show_table_orders(table_number)  # Ενημερώστε τον πίνακα για το τραπέζι


        

    def create_show_table_orders_function(self, table_number):
        def button_clicked():
            self.active_table_number = table_number
            self.last_active_table = table_number  # Ενημερώστε το last_active_table
            self.show_table_orders(table_number)
        return button_clicked

    def update_buttons(self):
        # Διαγραφή των παλιών κουμπιών
        while self.gridLayout_button.count():
            child = self.gridLayout_button.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        # Ανακτήστε τα τρέχοντα δεδομένα και δημιουργήστε τα νέα κουμπιά
        self.initialize_buttons()
        if self.last_active_table is not None:
           self.show_table_orders(self.last_active_table)  # Φορτώστε τις παραγγελίες για το ενεργό τραπέζι

    def darken_color(self, color):
        import colorsys
        if color.startswith('rgb'):
            color = color[4:-1].split(',')
            color = [int(c) / 255.0 for c in color]
            r, g, b = colorsys.rgb_to_hls(*color)
            r, g, b = colorsys.hls_to_rgb(r, max(0, g - 0.1), b)
            return f"rgb({int(r * 255)}, {int(g * 255)}, {int(b * 255)})"
        return color

    def initialize_buttons(self):
        sorted_tables = self.read_and_sort_tables('shared_data/occupied_tables.json')

        orders_status = self.fetch_order_status('example.db')

        scroll_area = QScrollArea(self.frame_23)
        scroll_area.setWidgetResizable(True)

        scroll_widget = QWidget()
        grid_layout = QGridLayout(scroll_widget)
        grid_layout.setSpacing(10)
        grid_layout.setContentsMargins(10, 10, 10, 10)

        num_columns = 2
        for i, table in enumerate(sorted_tables):
            table_number = table["table_number"]

            color = self.check_order_status(table_number)
            if color == "rgb(255, 255, 255)":
                continue  # Παραλείψτε τα λευκά κουμπιά

            container_widget = QWidget()
            vbox = QVBoxLayout(container_widget)
            vbox.setSpacing(2)
            vbox.setContentsMargins(0, 0, 0, 0)

            button = QPushButton(f"{table_number}", container_widget)
            button.setMinimumSize(71, 61)

            darker_color = self.darken_color(color)
            button.setStyleSheet(f"""
                QPushButton {{
                    background-color: {color};
                    border: none;
                    text-align: center;
                    font-size: 18px;
                    color: white;
                    font-weight: bold;
                    padding-bottom: 1px;
                    border-radius: 5px;
                }}
                QPushButton:hover {{
                    background-color: {darker_color};
                }}
                QPushButton:checked {{
                    border: 2px solid #428985;
                }}
            """)

            vbox.addWidget(button)

            if table_number in orders_status and orders_status[table_number]['orders_not_done'] > 0:
                status = orders_status[table_number]
                info_label = QLabel(f"Pending: {status['orders_not_done']}", container_widget)
                vbox.addWidget(info_label)
                info_label.setStyleSheet("""
                    QLabel {
                        font-size: 13px;
                        text-align: center;
                        margin-top: -25px;
                    }
                """)
                info_label.setAlignment(Qt.AlignCenter)

            row = i // num_columns
            col = i % num_columns
            grid_layout.addWidget(container_widget, row, col)

            button.clicked.connect(self.create_show_table_orders_function(table_number))
            if self.last_active_table == table_number:
                button.setStyleSheet(f"background-color: {color}; border: 9px solid yellow;")
                self.show_table_orders(self.last_active_table)

        scroll_area.setWidget(scroll_widget)
        self.gridLayout_button.addWidget(scroll_area, 0, 0, 1, 1)

    def read_and_sort_tables(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        tables = data["tables"]
        sorted_tables = sorted(tables, key=lambda x: self.convert_duration_to_seconds(x["duration"]), reverse=True)
        
        return sorted_tables

    def convert_duration_to_seconds(self, duration):
        days = 0
        hours = 0
        minutes = 0
        seconds = 0

        if 'day' in duration or 'days' in duration:
            parts = duration.split(',')
            days_part = parts[0].strip()
            time_part = parts[1].strip() if len(parts) > 1 else '0:0:0'

            # Απόσπαση των ημερών
            days = int(days_part.split()[0])

            # Απόσπαση των ωρών, λεπτών, και δευτερολέπτων
            time_parts = time_part.split(':')
            if len(time_parts) == 3:
                hours, minutes, seconds = map(int, time_parts)
            elif len(time_parts) == 2:
                hours, minutes = map(int, time_parts)

        else:
            time_parts = duration.split(':')
            if len(time_parts) == 3:
                hours, minutes, seconds = map(int, time_parts)
            elif len(time_parts) == 2:
                hours, minutes = map(int, time_parts)

        total_seconds = (days * 86400) + (hours * 3600) + (minutes * 60) + seconds
        return total_seconds

    def show_already_printed_message(self):
        QMessageBox.information(self, "Προειδοποίηση", "Η παραγγελία έχει ήδη εκτυπωθεί!")        
        
    def check_order_status(self, table_number):
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()

        # Ελέγξτε για παραγγελίες που έχουν ολοκληρωθεί αλλά δεν έχουν εκτυπωθεί
        cursor.execute("SELECT COUNT(*) FROM orders WHERE table_number = ? AND order_done = 1 AND printed = 0", (table_number,))
        if cursor.fetchone()[0] > 0:
            conn.close()
            return "rgb(0, 255, 0)"  # Πράσινο χρώμα για παραγγελίες που πρέπει να εκτυπωθούν

        # Ελέγξτε για παραγγελίες που δεν έχουν ολοκληρωθεί
        cursor.execute("SELECT COUNT(*) FROM orders WHERE table_number = ? AND order_done = 0", (table_number,))
        if cursor.fetchone()[0] > 0:
            conn.close()
            return "rgb(255, 0, 0)"  # Κόκκινο χρώμα για παραγγελίες που δεν έχουν ολοκληρωθεί

        conn.close()
        return "rgb(255, 255, 255)"  # Λευκό χρώμα για τραπέζια χωρίς ενεργές παραγγελίες

    def onSubmit(self):
        category = self.lineEdit_category.text()
        description = self.lineEdit_description.text()
        price = self.lineEdit_price.text()
        amount = self.lineEdit_amount.text()
        
        if self.validate_input(category, description, price, amount):
            add_record(category, description, price, amount)
            # Ανανέωση της λίστας με τις τρέχουσες εγγραφές
            self.refresh_list_view()
            self.clear_input_fields()
        else:
            print("Σφάλμα: Μη έγκυρη εισαγωγή δεδομένων")

    def clear_input_fields(self):
        self.lineEdit_category.clear()
        self.lineEdit_description.clear()
        self.lineEdit_price.clear()
        self.lineEdit_amount.clear()

    def onCategoryTextChanged(self, text):
        # Αναζητήστε τις εγγραφές και ενημερώστε το model_category
        results = search_database("category", text)
        self.updateListView(self.model_category, results)

    def onDescriptionTextChanged(self, text):
        # Αναζητήστε τις εγγραφές και ενημερώστε το model_description
        results = search_database("description", text)
        self.updateListView(self.model_description, results)

    def updateListView(self, model, results):
        model.clear()  # Καθαρισμός του μοντέλου
        for item in results:
            item_str = " - ".join(map(str, item[1:]))  # Αποκλείστε το id
            model.appendRow(QStandardItem(item_str))

    def onListViewCategoryClicked(self, index):
        # Ενημερώστε τα QLineEdit με την επιλεγμένη εγγραφή
        item = self.model_category.itemFromIndex(index)
        self.updateLineEdits(item.text())

    def onListViewDescriptionClicked(self, index):
        # Ενημερώστε τα QLineEdit με την επιλεγμένη εγγραφή
        item = self.model_description.itemFromIndex(index)
        self.updateLineEdits(item.text())

    def updateLineEdits(self, text):
        parts = text.split(" - ", maxsplit=3)
        if len(parts) == 4:
            category, description, price, amount = parts
            self.lineEdit_category.setText(category)
            self.lineEdit_description.setText(description)
            self.lineEdit_price.setText(price)
            self.lineEdit_amount.setText(amount)
        else:
            print("Σφάλμα: Αναμενόταν συμβολοσειρά με τέσσερα μέρη")

    def updateListWidget(self, category, description, price, amount):
        entry = f"{category} - {description} - {price} - {amount}"
        print("Προσθήκη στη λίστα:", entry)
        item = QStandardItem(entry)
        self.productListView.insertRow(0, item)

    def onListItemClicked(self, index):
        # Λήψη του στοιχείου από το μοντέλο
        item = self.productListModel.itemFromIndex(index)
        if item:
            text = item.text()
            # Διαχωρισμός του κειμένου και ενημέρωση των QLineEdit
            try:
                category, description, price, amount = text.split(" - ", maxsplit=3)
                self.lineEdit_category.setText(category)
                self.lineEdit_description.setText(description)
                self.lineEdit_price.setText(price)
                self.lineEdit_amount.setText(amount)
            except ValueError as e:
                print("Σφάλμα κατά τη διάσπαση της συμβολοσειράς:", e)

    def validate_input(self, category, description, price, amount):
        # Έλεγχος για διπλοτυπία
        if self.check_duplicate_description(description):
            self.show_error_message("Υπάρχει ήδη αυτό το προϊόν.")
            return False
        # Έλεγχος πληρότητας
        if not all([category, description, price, amount]):
            self.show_error_message("Όλα τα πεδία πρέπει να συμπληρωθούν.")
            return False
        # Έλεγχος εγκυρότητας αριθμητικών δεδομένων
        try:
            float(price)
            int(amount)
        except ValueError:
            self.show_error_message("Το πεδίο τιμής πρέπει να είναι αριθμός και η ποσότητα πρέπει να είναι ακέραιος αριθμός.")
            return False

        return True

    def delete_record(record_id): # type: ignore
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM products WHERE id = ?', (record_id,))
            conn.commit()
            print("Διαγραφή επιτυχής")
        except Exception as e:
            print("Σφάλμα κατά τη διαγραφή:", e)
        finally:
            conn.close()

    def delete_selected_record(self):
        selected_indexes = self.productListView.selectedIndexes()
        if not selected_indexes:
            print("Δεν έχει επιλεγεί καμία εγγραφή")
            return

        reply = QMessageBox.question(self, 'Διαγραφή Εγγραφής', 'Είστε σίγουροι πως θέλετε να διαγράψετε την επιλεγμένη εγγραφή;', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            for index in selected_indexes:
                # Υποθέτουμε ότι ο κωδικός (ID) του προϊόντος αποθηκεύεται ως UserRole στο μοντέλο
                record_id = self.productListModel.data(index, Qt.UserRole)
                delete_record(record_id)  # Συνάρτηση για διαγραφή εγγραφής από τη βάση δεδομένων
                self.productListModel.removeRow(index.row())

            self.refresh_list_view()

    def refresh_list_view(self):
        results = self.get_all_records()
        self.updateListView(self.productListModel, results)
        
    def get_all_records(self):
        try:
            conn = sqlite3.connect('products.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM products")
            results = cursor.fetchall()
            conn.close()
            return results
        except Exception as e:
            print(f"Σφάλμα κατά την ανάκτηση εγγραφών: {e}")
            return []

    def check_duplicate_description(self, description):
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE description = ?", (description,))
        results = cursor.fetchall()
        conn.close()
        return len(results) > 0

    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(message)
        msg.setWindowTitle("Σφάλμα Εισαγωγής")
        msg.exec()  # Αντικατάσταση της 'exec_()' με 'exec()'
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            self.delete_selected_record()

    def delete_selected_item(self):
        selected_indexes = self.productListView.selectedIndexes()
        if not selected_indexes:
            print("Δεν έχει επιλεγεί καμία εγγραφή")
            return

        reply = QMessageBox.question(self, 'Διαγραφή Εγγραφής', 'Είστε σίγουροι πως θέλετε να διαγράψετε την επιλεγμένη εγγραφή;', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            for index in selected_indexes:
                record_id = self.productListModel.data(index, Qt.UserRole)  # Προσαρμόστε ανάλογα
                delete_record(record_id)  # Η λειτουργία διαγραφής από τη βάση
                self.productListModel.removeRow(index.row())

            self.refresh_list_view()

    def insert_into_database(self, category, description, price, amount):
        try:
            add_record(category, description, price, amount)
            print("Επιτυχής εισαγωγή εγγραφής στη βάση δεδομένων.")
            self.export_to_json()
        except Exception as e:
            print(f"Σφάλμα κατά την εισαγωγή: {e}")

    def export_to_json(self):
        try:
            records = self.get_all_records()
            data = {"products": []}
            for record in records:
                id, category, description, price, amount = record
                data["products"].append({
                    "id": id,
                    "category": category,
                    "description": description,
                    "price": price,
                    "amount": amount
                })
            with open(os.path.join("shared_data", "products.json"), "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            print("Τα δεδομένα εξήχθησαν επιτυχώς σε JSON.")
        except Exception as e:
            print(f"Σφάλμα κατά την εξαγωγή σε JSON: {e}")

    def initialize_tables(self):
        image_path = 'tables_visualization.jpg'

        # Λήψη των διαστάσεων του QGraphicsView (ή άλλου widget) απευθείας
        self.view_width = self.graphicsView.width()
        self.view_height = self.graphicsView.height()

        # Φόρτωση της εικόνας και λήψη διαστάσεων
        self.image_width, self.image_height = self.get_image_dimensions(image_path) # type: ignore

        # Φόρτωση των δεδομένων τραπεζιών
        tables_placement = self.read_table_data()  

        # Κλήση της add_tables_to_scene με τα ενημερωμένα δεδομένα
        self.add_tables_to_scene(tables_placement, self.image_width, self.image_height)

    def read_table_data(self):
        tables_placement = []
        try:
            with open('tables.txt', 'r') as file:
                for line in file:
                    parts = line.strip().split()
                    if len(parts) == 5:
                        id, x1, y1, x2, y2 = map(int, parts)
                        center_x = (x1 + x2) / 2
                        center_y = (y1 + y2) / 2
                        tables_placement.append({'id': id, 'center_x': center_x, 'center_y': center_y})
        except Exception as e:
            print(f"Error reading file: {e}")
        return tables_placement

    def get_image_dimensions(self, image_path):
        try:
            image = QPixmap(image_path)
            return image.width(), image.height()
        except Exception as e:
            print(f"Error opening image: {e}")
            return None
    
    def load_occupied_tables(self):
        try:
            with open('shared_data/occupied_tables.json', 'r') as file:
                data = json.load(file)
                return data['tables']
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    def is_table_reserved(self, table_number):
        today = QDate.currentDate().toString("yyyy-MM-dd")
        conn = sqlite3.connect('reserve.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM reserve WHERE date = ? AND table_number = ?', (today, table_number))
        count = cursor.fetchone()[0]
        conn.close()
        return count > 0

    def add_tables_to_scene(self, tables_placement, image_width, image_height):
        self.scene.clear()
        
        occupied_tables_info = self.load_occupied_tables()
         # Δημιουργία λεξικού για ταχύτερη πρόσβαση
        occupied_info_dict = {str(table["table_number"]): table for table in occupied_tables_info}
        
        num_tables = len(tables_placement)
        if num_tables == 0: return  # Έξοδος εάν δεν υπάρχουν τραπέζια

        padding = 5 # Προσθέστε ένα περιθώριο από κάθε πλευρά του τραπεζιού

        # Υπολογισμός διαστάσεων πλέγματος
        rows = round(math.sqrt(num_tables))
        cols = math.ceil(num_tables / rows)

        # Καθορισμός διαστάσεων τραπεζιών με το περιθώριο
        table_width = (self.view_width / cols) - (2 * padding)
        table_height = (self.view_height / rows) - (2 * padding)

        # Τοποθέτηση τραπεζιών
        for i, table in enumerate(tables_placement):
            grid_x = i % cols
            grid_y = i // cols

            x = (grid_x * (self.view_width / cols)) + padding
            y = (grid_y * (self.view_height / rows)) + padding

            table_id = str(table.get('id', 'Unknown'))
            table_info = occupied_info_dict.get(table_id)

            # Αλλαγή χρώματος ανάλογα με το αν το τραπέζι είναι κατειλημμένο
            color = QColor("green")  # Πράσινο για διαθέσιμο
            if table_info and table_info['occupied_since']:
                color = QColor("red")  # Κόκκινο για κατειλημμένο

            rect = QGraphicsRectItem(x, y, table_width, table_height)
            rect.setBrush(color)
            self.scene.addItem(rect)
            
            table_id = str(table.get('id', 'Unknown'))
            reserved = self.is_table_reserved(table_id)

            # Προσθέστε το "R" στο κείμενο αν το τραπέζι είναι κρατημένο
            table_text = f"{table_id}R" if reserved else table_id

            # Δημιουργία και τοποθέτηση του κειμένου τραπεζιού
            text = QGraphicsTextItem(table_id)
            text.setFont(QFont("Arial", 13))
            text.setPos(x + (table_width - text.boundingRect().width()) / 2, y + (table_height - text.boundingRect().height()) / 2)
            self.scene.addItem(text)

            # Εάν το τραπέζι είναι κρατημένο, προσθέστε τη λέξη "RESERVE" στο επάνω μέρος του
            if reserved:
                reserve_text = QGraphicsTextItem("RESERVE")
                reserve_text.setFont(QFont("Arial", 13))
                reserve_text.setDefaultTextColor(Qt.black)
                reserve_text.setPos(x + (table_width - reserve_text.boundingRect().width()) / 2, y)
                self.scene.addItem(reserve_text)

    def check_for_new_day(self):
        current_date = QDate.currentDate()
        if current_date != self.last_checked_date:
            self.reset_database_data()
            self.last_checked_date = current_date 
            
    def reset_database_data(self):
        reply = QMessageBox.question(self, 'Επιβεβαίωση Διαγραφής', 'Είστε σίγουροι ότι θέλετε να διαγράψετε όλα τα δεδομένα;', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            conn = sqlite3.connect('tables_occupation.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tables")
            conn.commit()
            conn.close()    
            
    def set_notify_limit_value(self):
        self.notify_limit = self.spinBox_notify_minutes.value()
        
        self.update_tables_view()
   
    def convert_duration(self, duration):
        days = 0
        hours = 0
        minutes = 0

        parts = duration.split(',')

        if 'day' in parts[0] or 'days' in parts[0]:
            days = int(parts[0].split()[0])
            if len(parts) > 1:
                time_part = parts[1].strip()
                time_parts = time_part.split(':')
                hours = int(time_parts[0]) if time_parts[0] else 0
                minutes = int(time_parts[1]) if len(time_parts) > 1 and time_parts[1] else 0
        else:
            time_parts = parts[0].split(':')
            hours = int(time_parts[0]) if time_parts[0] else 0
            minutes = int(time_parts[1]) if len(time_parts) > 1 and time_parts[1] else 0

        total_minutes = (days * 24 * 60) + (hours * 60) + minutes
        return total_minutes

    def get_current_status(self):
        while True:
            try:
                conn = sqlite3.connect('example.db')
                cursor = conn.cursor()

                # Ερώτηση για την ανάκτηση των τελευταίων 100 εγγραφών
                cursor.execute("""
                    SELECT table_number, order_done
                    FROM orders
                    ORDER BY id DESC
                    LIMIT 150
                """)
                last_100_orders = cursor.fetchall()
                conn.close()

                # Δημιουργία ενός λεξικού για να αποθηκεύσουμε την κατάσταση κάθε τραπεζιού
                table_status = {}
                for table_number, order_done in last_100_orders:
                    if table_number not in table_status:
                        table_status[table_number] = True  # Αρχική υπόθεση ότι όλες οι παραγγελίες έχουν ολοκληρωθεί
                    table_status[table_number] = table_status[table_number] and (order_done == 1)

                # Φιλτράρισμα των τραπεζιών που όλες οι εγγραφές είναι με order_done = 1
                tables_with_all_orders_completed = [table_number for table_number, all_completed in table_status.items() if all_completed]

                return tables_with_all_orders_completed
            
            except sqlite3.OperationalError:
                print("Η βάση δεδομένων είναι κλειδωμένη. Περιμένω πριν δοκιμάσω ξανά.")
                time.sleep(1)  # Περιμένει για 1 δευτερόλεπτο πριν δοκιμάσει ξανά

    def find_row_by_table_number(self, table_number):
        # Αναζητά τη γραμμή στο QTableView που αντιστοιχεί στο δοθέν table_number
        for row in range(self.tableView.rowCount()):
            if self.tableView.item(row, 0) and self.tableView.item(row, 0).text() == str(table_number):
                return row
        return None  
    
    def check_order_delivered(self, table_number):
        try:
            print(f"Έλεγχος για το τραπέζι {table_number}")
            # Σύνδεση με τη βάση δεδομένων
            conn = sqlite3.connect('example.db')
            cursor = conn.cursor()

            # Εκτέλεση του ερωτήματος
            query = "SELECT printed, order_done FROM orders WHERE table_number = ?"
            cursor.execute(query, (table_number,))
            result = cursor.fetchone()
                       
            # Κλείσιμο της σύνδεσης με τη βάση δεδομένων
            cursor.close()
            conn.close()

            # Ελέγξτε αν το αποτέλεσμα ικανοποιεί τα κριτήρια
            if result and result[0] == 1 and result[1] == 1:
                print(f"Τραπέζι {table_number}: Delivered")
                return True
            else:
                print(f"Τραπέζι {table_number}: Not Delivered")
                return False

        except sqlite3.Error as e:
            print(f"Σφάλμα στη βάση δεδομένων: {e}")
            # Επιστρέψτε False ή χειριστείτε το σφάλμα ανάλογα
            return False

    # Ενημέρωση της εμφάνισης του LED ανάλογα με την κατάσταση του χρονοδιακόπτη
    def update_led(self, color):
        # Επιλογή του σωστού εικονιδίου και προσαρμογή του μεγέθους του
        if color == "green":
            pixmap = self.green_led_icon.scaled(self.green_led.width(), self.green_led.height(), Qt.KeepAspectRatio)
            item = QGraphicsPixmapItem(pixmap)
        else:  # Default σε κόκκινο εικονίδιο
            pixmap = self.red_led_icon.scaled(self.red_led.width(), self.red_led.height(), Qt.KeepAspectRatio)
            item = QGraphicsPixmapItem(pixmap)

        scene = QGraphicsScene(self)
        scene.addItem(item)

        # Ενημέρωση της σκηνής ανάλογα με το επιλεγμένο χρώμα LED
        if color == "green":
            self.green_led.setScene(scene)
            self.red_led.setScene(None)
        else:
            self.red_led.setScene(scene)
            self.green_led.setScene(None)

    # Ανανέωση της ρύθμισης του χρονοδιακόπτη βάσει της τιμής του QSpinBox
    def update_timer(self):
        interval = self.timer_spinBox.value() * 1000  # Μετατροπή λεπτών σε χιλιοστά του δευτερολέπτου
        if interval > 0:
            self.timer.start(interval)
          
        else:
            self.timer.stop()

    def load_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Load Image", "", "Image Files (*.png; *.jpg; *.jpeg)", options=options)
        if file_name:
            self.image_path = file_name
            self.update_image(file_name)

    def update_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.graphicsScene.clear()
        self.graphicsScene.addPixmap(pixmap)
        self.graphicsView.setSceneRect(pixmap.rect())  # Ορίζει τα όρια της σκηνής βάσει της εικόνας
        # Προσαρμόζει την εικόνα στο QGraphicsView διατηρώντας τις αναλογίες της
        self.graphicsView.fitInView(pixmap.rect(), Qt.KeepAspectRatio)
   
    def update_data(self):
        with open('shared_data/occupied_tables.json', 'r') as file:
            data = json.load(file)

        conn = sqlite3.connect('tables_occupation.db')
        cursor = conn.cursor()

        for table in data["tables"]:
            table_number = table["table_number"]
            occupied_since = table["occupied_since"]
            duration = table["duration"]
            center_coordinates = str(table["center_coordinates"]) if "center_coordinates" in table else None

            record_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Καταγραφή της τρέχουσας ώρας

            cursor.execute('''
                INSERT INTO tables (table_id, occupied_since, duration, center_coordinates, record_time)
                VALUES (?, ?, ?, ?, ?)
                ''', (table_number, occupied_since, duration, center_coordinates, record_time))

        conn.commit()
        conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    username = sys.argv[1] if len(sys.argv) > 1 else 'default_username'
    main_window = MainWindow(username=username)  # Στέλνουμε το username ως keyword argument
    main_window.show()
    sys.exit(app.exec())
