import sys
import subprocess
import requests
from requests.exceptions import RequestException, Timeout
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QProgressDialog
from PySide6.QtCore import QTimer, QUrl, Qt
from PySide6.QtGui import QDesktopServices
from LoginWindow_ui import Ui_MainWindow  # Ensure this file is generated from the provided XML
import logging

import connect
import z

# Δημιουργία logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Handler που θα γράφει logs σε αρχείο
file_handler = logging.FileHandler('z_app.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Handler που θα εμφανίζει logs στην κονσόλα
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Προσθήκη των handlers στο logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

class LoginWindow(QMainWindow):
    _instance = None

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        if self._instance is not None:
            raise Exception("This class is a singleton!")
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.session = requests.Session()
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.register_button.clicked.connect(self.open_registration_page)
        self.ui.lineEdit.setEchoMode(QLineEdit.Password)
        self.z_process = None
        self.connect_process = None
        self._instance = self
        logger.debug("LoginWindow initialized")

    def start_processes(self):
        self.z_process = subprocess.Popen(
            [sys.executable, '-c', f'import z; z.main_function("{self.usernameLoggedIn}")'],
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True
        )
        self.connect_process = subprocess.Popen(
            [sys.executable, '-c', f'import connect; connect.main_function("{self.usernameLoggedIn}")'],
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True
        )
        logger.debug("z_process and connect_process started")
        self.check_z_process()

    def check_z_process(self):
        logger.debug("Checking z_process status")
        if self.z_process.poll() is None:
            logger.info('z.py is still running')
            QTimer.singleShot(500, self.check_z_process)
        else:
            stdout, stderr = self.z_process.communicate()
            logger.debug(f"z_process terminated, stdout: {stdout}, stderr: {stderr}")
            if stdout:
                logger.info(f'z.py finished. Output: {stdout}')
            if stderr:
                logger.error(f'z.py error: {stderr}')

    def terminate_connect_process(self):
        if self.connect_process and self.connect_process.poll() is None:
            self.connect_process.terminate()
            logger.info("connect.py process terminated")

    def get_csrf_token(self):
        try:
            logger.debug("Attempting to get CSRF token...")
            response = self.session.get('http://localhost:8003/authentication/get-csrf-token/', timeout=10)
            logger.debug(f"CSRF token request response: {response.status_code}")
            if response.status_code == 200:
                csrf_token = response.json().get('csrfToken')
                logger.debug(f"CSRF token received: {csrf_token}")
                return csrf_token
            else:
                logger.error(f"Failed to get CSRF token, status code: {response.status_code}, response content: {response.content}")
        except RequestException as e:
            logger.error(f"Failed to get CSRF token: {e}")
        return None

    def login(self):
        username = self.ui.lineEdit_2.text()
        password = self.ui.lineEdit.text()
        csrf_token = self.get_csrf_token()
        if not csrf_token:
            QMessageBox.critical(self, 'Σφάλμα', 'Αποτυχία λήψης CSRF token.')
            return

        headers = {
            'X-CSRFToken': csrf_token,
            'Referer': 'http://localhost:8003/authentication/login/',
        }

        try:
            logger.debug(f"Attempting to login with username: {username}")
            response = self.session.post(
                'http://localhost:8003/authentication/login/',
                data={'username': username, 'password': password},
                headers=headers,
                timeout=15
            )
            logger.debug(f"Login request sent, awaiting response...")
            if response.status_code == 200:
                self.usernameLoggedIn = username
                logger.debug("Login successful")
                QTimer.singleShot(100, self.openMainApp)
            else:
                logger.warning(f"Failed login attempt, status code: {response.status_code}, response content: {response.content}")
                QMessageBox.warning(self, 'Σφάλμα', 'Λάθος όνομα χρήστη ή κωδικός.')
        except Timeout:
            logger.error("The server did not respond in time.")
            QMessageBox.critical(self, 'Σφάλμα', 'Ο server δεν ανταποκρίθηκε εγκαίρως. Παρακαλώ δοκιμάστε ξανά αργότερα.')
        except RequestException as e:
            logger.error(f"Login failed with error: {e}")
            QMessageBox.critical(self, 'Σφάλμα', f'Πρόβλημα στην σύνδεση: {e}')

    def openMainApp(self):
        self.showProgressDialog()
        self.start_processes()
        QTimer.singleShot(5100, self.close)

    def showProgressDialog(self):
        progress_dialog = QProgressDialog("Loading, please wait...", None, 0, 100, self)
        progress_dialog.setWindowFlag(Qt.FramelessWindowHint)
        progress_dialog.setModal(True)

        progress_dialog.setStyleSheet("""
        QProgressDialog {
            background-color: #f0f0f0;
            border: 1px solid #ccc;
            border-radius: 10px;
            padding: 15px;
        }
        QLabel {
            color: #447781;
            font: 10pt "Segoe UI";
        }
        QProgressBar {
            border: 1px solid #ccc;
            border-radius: 20px;
            text-align: center;
            height: 20px;
            color: white;
        }
        QProgressBar::chunk {
            background-color: blue;
            width:120px;
            height: 10px;
            color:white;
        }
        """)

        progress_dialog.show()

        for i in range(101):
            QTimer.singleShot(i * 50, lambda value=i: progress_dialog.setValue(value))

        QTimer.singleShot(10000, progress_dialog.close)

    def open_registration_page(self):
        registration_url = QUrl("http://localhost:8003/authentication/register/")
        QDesktopServices.openUrl(registration_url)

    def closeEvent(self, event):
        self.session.close()

def main():
    app = QApplication(sys.argv)
    login_window = LoginWindow.getInstance()
    login_window.show()
    app.exec()

if __name__ == "__main__":
    main()
