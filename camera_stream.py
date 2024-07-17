import sys
import socket
import ipaddress
import cv2
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsPixmapItem, QGraphicsScene, QLabel, QLineEdit, QPushButton, QMessageBox, QProgressBar, QListView, QStatusBar
from PySide6.QtCore import QThread, Signal, Qt, QTimer, QEventLoop
from PySide6.QtGui import QImage, QPixmap, QStandardItemModel, QStandardItem
import json
import os
from ip_camera_scan_ui import Ui_MainWindow
import numpy as np
import asyncio
from concurrent.futures import ThreadPoolExecutor
from onvif import ONVIFCamera
import datetime

# Θύρες που ενδεχομένως χρησιμοποιούνται από κάμερες
CAMERA_PORTS = [80, 8080, 8003, 10080, 10554]

# IP διευθύνσεις που είναι συνήθως router
COMMON_ROUTER_IPS = ["192.168.1.1", "192.168.1.256", "192.168.2.1"]

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port} on IP {ip} is open")
                return port
            else:
                print(f"Port {port} on IP {ip} is closed with result {result}")
    except Exception as e:
        print(f"Error scanning port {port} on IP {ip}: {e}")
    return None

def scan_ports(ip, ports):
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(lambda port: scan_port(ip, port), ports)
        open_ports = [port for port in results if port is not None]
    return open_ports

async def get_onvif_data(ip, port, user, passw, loop):
    executor = ThreadPoolExecutor()
    try:
        mycam = ONVIFCamera(ip, port, user, passw, no_cache=True)
        media_service = await loop.run_in_executor(executor, mycam.create_media_service)
        device_service = await loop.run_in_executor(executor, mycam.create_devicemgmt_service)

        # Device Information
        device_info = await loop.run_in_executor(executor, device_service.GetDeviceInformation)

        # Profiles and Media Information
        profiles = await loop.run_in_executor(executor, media_service.GetProfiles)
        media_info = {'profiles': [], 'stream_uri': None}

        for profile in profiles:
            try:
                request = media_service.create_type('GetStreamUri')
                request.ProfileToken = profile.token
                request.StreamSetup = {'Stream': 'RTP-Unicast', 'Transport': {'Protocol': 'RTSP'}}
                stream_uri = await loop.run_in_executor(executor, media_service.GetStreamUri, request)
                media_info['stream_uri'] = stream_uri.Uri
                media_info['profiles'].append({
                    'name': profile.Name,
                    'token': profile.token,
                    'width': profile.VideoEncoderConfiguration.Resolution.Width,
                    'height': profile.VideoEncoderConfiguration.Resolution.Height
                })
            except Exception as e:
                print(f"Error retrieving stream URI for {ip} on port {port}: {e}")
                continue

        return {
            'device_info': {
                'Manufacturer': device_info.Manufacturer,
                'Model': device_info.Model,
                'FirmwareVersion': device_info.FirmwareVersion,
                'SerialNumber': device_info.SerialNumber 
            },
            'media_info': media_info
        }
    except Exception as e:
        print(f"Error connecting to ONVIF camera {ip} on port {port}: {e}")
        return {'error': str(e)}
    finally:
        executor.shutdown()

async def try_onvif_connection(ip, ports, progress_callback, camera_found_signal, stop_event):
    loop = asyncio.get_running_loop()
    with open('camera_data.json', 'r') as file:
        credentials_list = json.load(file)

    if not isinstance(credentials_list, list) or not all(isinstance(cred, dict) for cred in credentials_list):
        print("Error: Credentials data is malformed or not in expected list of dictionaries format.")
        return None

    for creds in credentials_list:
        if stop_event.is_set():
            break
        user, passw = creds.get('username'), creds.get('password')
        if not user or not passw:
            print("Error: Missing username or password in credentials.")
            continue

        for port in ports:
            if stop_event.is_set():
                break
            onvif_data = await get_onvif_data(ip, port, user, passw, loop)
            if onvif_data and 'error' not in onvif_data:
                print(f"Valid credentials found for {ip} on port {port}: {user}/{passw}")
                print(f"ONVIF Data for {ip} on port {port}: {json.dumps(onvif_data, indent=4)}")
                camera_data = {
                    'ip': ip,
                    'mac': 'Unknown',
                    'vendor': 'Unknown',
                    'ports': ports,
                    'confirmed': 0,
                    'username': user,
                    'password': passw,
                    'name_of_camera': creds.get('name_of_camera', 'Unknown'),
                    'onvif': onvif_data
                }
                save_camera_to_json(camera_data, 'camera_results.json')
                camera_found_signal.emit(camera_data)
                return camera_data
            else:
                print(f"Invalid credentials for {ip} on port {port}: {user}/{passw}")
    return None

async def scan_specific_ips(ips, progress_callback, camera_found_signal, stop_event):
    cameras = []
    for ip in ips:
        if stop_event.is_set():
            break
        print(f"Scanning specific IP: {ip}")
        open_ports = scan_ports(ip, CAMERA_PORTS)
        if open_ports:
            camera_data = await try_onvif_connection(ip, open_ports, progress_callback, camera_found_signal, stop_event)
            if camera_data:
                cameras.append(camera_data)
                print(f"IP: {ip} Open ports: {open_ports}")
                break
        progress_callback.emit(1)
    return cameras

async def scan_network(subnet, progress_callback, camera_found_signal, stop_event):
    cameras = []
    network = ipaddress.ip_network(subnet, strict=False)
    ip_list = list(network.hosts())[:256]
    for ip in ip_list:
        if stop_event.is_set():
            break
        ip = str(ip)
        print(f"Scanning IP: {ip}")
        open_ports = scan_ports(ip, CAMERA_PORTS)
        if open_ports:
            camera_data = await try_onvif_connection(ip, open_ports, progress_callback, camera_found_signal, stop_event)
            if camera_data:
                cameras.append(camera_data)
                print(f"IP: {ip} Open ports: {open_ports}")
        progress_callback.emit(1)
    return cameras

async def discover_cameras(subnets, progress_callback, camera_found_signal, stop_event):
    cameras = []
    # Σάρωση των συνήθων IP των router
    cameras += await scan_specific_ips(COMMON_ROUTER_IPS, progress_callback, camera_found_signal, stop_event)
    if not cameras:
        # Αν δεν βρεθεί ανοιχτή θύρα στις συνήθεις IP, σαρώνουμε όλα τα subnets
        for subnet in subnets:
            cameras += await scan_network(subnet, progress_callback, camera_found_signal, stop_event)
    return cameras

def save_camera_to_json(camera_data, file_path):
    try:
        with open(file_path, 'r') as json_file:
            cameras = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        cameras = []

    # Αφαίρεση παλιών εγγραφών για την ίδια κάμερα (όνομα) και διαφορετική IP
    cameras = [cam for cam in cameras if not (cam['name_of_camera'] == camera_data['name_of_camera'] and cam['ip'] != camera_data['ip'])]

    # Αφαίρεση παλιών εγγραφών για την ίδια κάμερα (όνομα) και ίδια IP
    cameras = [cam for cam in cameras if not (cam['name_of_camera'] == camera_data['name_of_camera'] and cam['ip'] == camera_data['ip'])]

    cameras.append(camera_data)

    with open(file_path, 'w') as json_file:
        json.dump(cameras, json_file, indent=4)

def load_timer_interval():
    with open('parameters.json', 'r') as file:
        params = json.load(file)
    return params['timer_interval']

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.lineEdit_username.setPlaceholderText("Enter username")
        self.lineEdit_password.setPlaceholderText("Enter password")
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.pushButton_add_camera.clicked.connect(self.create_camera_json)
        self.load_camera_names()
        self.cap = None  # Αρχικοποίηση της ιδιότητας cap

        self.timer = QTimer()  # Αρχικοποίηση του timer
        self.timer.timeout.connect(self.update_frame)
        
        self.init_timer()  # Εισαγωγή του νέου χρονοδιακόπτη για snapshots

        self.check_and_start_streams()

        self.progressBar.hide()  # Αρχικά κρυμμένο

        if self.listView_founded_names_of_cameras:
            self.listView_founded_names_of_cameras.doubleClicked.connect(self.on_camera_double_clicked)
        
        self.RenewIP.clicked.connect(self.run_external_script)
        self.Stop_searching_button.clicked.connect(self.stop_search)

        self.discovery_thread = None
        self.streaming = False

    def init_timer(self):
        timer_interval = load_timer_interval() * 1000  # Μετατροπή σε ms
        self.snapshot_timer = QTimer(self)
        self.snapshot_timer.timeout.connect(self.take_snapshot)
        self.snapshot_timer.start(timer_interval)

    def take_snapshot(self):
        if self.cap and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                filename = f"tables_visualization.jpg"
                cv2.imwrite(filename, frame)
                print(f"Snapshot saved as {filename}")

    def on_camera_double_clicked(self, index):
        camera_name = self.listView_founded_names_of_cameras.model().itemFromIndex(index).text()
        self.setup_camera_stream(camera_name)

    def load_camera_names(self):
        json_path = os.path.join(os.path.dirname(__file__), 'camera_results.json')
        try:
            with open(json_path, 'r') as file:
                camera_data = json.load(file)
            
            if not camera_data:  # Έλεγχος αν η λίστα είναι κενή
                QMessageBox.warning(self, "Κανένα Αποτέλεσμα", "Δεν βρέθηκαν κάμερες. Ελέγξτε τη σύνδεση της κάμερας και προσπαθήστε ξανά.")
                return  # Διακοπή της εκτέλεσης της μεθόδου
            
            model = QStandardItemModel(self.listView_founded_names_of_cameras)
            for camera in camera_data:
                item = QStandardItem(camera['name_of_camera'])
                model.appendRow(item)
            self.listView_founded_names_of_cameras.setModel(model)
        except FileNotFoundError:
            QMessageBox.warning(self, "Αρχείο Δεν Βρέθηκε", "Το αρχείο camera_results.json δεν βρέθηκε.\nΕκτελέστε την αναζήτηση Renew IP.")
        except json.JSONDecodeError:
            QMessageBox.warning(self, "Διαβάστε Σφάλμα", "Σφάλμα κατά τη φόρτωση του αρχείου camera_results.json. Το αρχείο μπορεί να είναι κατεστραμμένο ή μη έγκυρο.")
        except Exception as e:
            QMessageBox.critical(self, "Σφάλμα", f"Απροσδιόριστο σφάλμα: {e}")

    def create_camera_json(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        name_of_camera = self.lineEdit_name_of_camera.text()

        new_camera_data = {
            "username": username,
            "password": password,
            "name_of_camera": name_of_camera
        }

        json_path = os.path.join(os.path.dirname(__file__), 'camera_data.json')

        try:
            with open(json_path, 'r') as file:
                existing_data = json.load(file)
            if not isinstance(existing_data, list):
                existing_data = []
            existing_data.append(new_camera_data)
        except FileNotFoundError:
            existing_data = [new_camera_data]

        with open(json_path, 'w') as file:
            json.dump(existing_data, file, indent=4)
        print("Camera data saved to 'camera_data.json'.")

    def display_selected_camera(self, current, previous):
        if current.isValid():
            camera_name = current.data()
            self.setup_camera_stream(camera_name)

    def setup_camera_stream(self, camera_name):
        json_path = os.path.join(os.path.dirname(__file__), 'camera_results.json')
        with open(json_path, 'r') as file:
            camera_data = json.load(file)
        for camera in camera_data:
            if camera['name_of_camera'] == camera_name:
                self.current_camera_name = camera_name
                stream_uri = camera['onvif']['media_info']['stream_uri']
                stream_uri = f"rtsp://{camera['username']}:{camera['password']}@{stream_uri.split('://')[1]}"
                if self.cap:
                    self.cap.release()
                self.cap = cv2.VideoCapture(stream_uri)
                if self.cap.isOpened():
                    self.timer.start(30)
                else:
                    self.remove_camera_from_json(camera)

    def update_frame(self):
        if self.cap:
            ret, frame = self.cap.read()
            if ret:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, f'{timestamp}', (10, frame.shape[0] - 10), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(frame, f'Camera: {self.current_camera_name}', (10, frame.shape[0] - 30), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
                p = convert_to_Qt_format.scaled(640, 480, Qt.KeepAspectRatio)
                pixmap = QPixmap.fromImage(p)
                item = QGraphicsPixmapItem(pixmap)
                if not hasattr(self, 'scene') or self.scene is None:
                    self.scene = QGraphicsScene()
                    self.graphicsView_camera1.setScene(self.scene)
                self.scene.clear()
                self.scene.addItem(item)

    def run_external_script(self):
        self.progressBar.show()
        self.progressBar.setValue(0)
        total_ips = 2 * 256
        self.progressBar.setMaximum(total_ips)

        self.discovery_thread = CameraDiscoveryThread(self)
        self.discovery_thread.progress.connect(self.update_progress)
        self.discovery_thread.camera_found.connect(self.handle_camera_found)
        self.discovery_thread.finished.connect(self.on_discovery_finished)
        self.discovery_thread.start()

    def stop_search(self):
        if self.discovery_thread is not None:
            self.discovery_thread.stop()
        self.progressBar.hide()

    def update_progress(self, value):
        self.progressBar.setValue(self.progressBar.value() + value)

    def handle_camera_found(self, camera_data):
        self.add_camera_to_list(camera_data)
        self.setup_camera_stream(camera_data['name_of_camera'])

    def add_camera_to_list(self, camera_data):
        model = self.listView_founded_names_of_cameras.model()
        if not model:
            model = QStandardItemModel(self.listView_founded_names_of_cameras)
            self.listView_founded_names_of_cameras.setModel(model)
        item = QStandardItem(camera_data['name_of_camera'])
        model.appendRow(item)

    def on_discovery_finished(self, cameras):
        self.progressBar.hide()
        self.load_camera_names()

    def cleanup_resources(self):
        if hasattr(self, 'cap') and self.cap and self.cap.isOpened():
            self.cap.release()
            print("Camera connection closed.")
        if hasattr(self, 'timer'):
            self.timer.stop()
            print("Timer stopped.")

    def closeEvent(self, event):
        self.cleanup_resources()
        event.accept()

    def remove_camera_from_json(self, camera):
        json_path = os.path.join(os.path.dirname(__file__), 'camera_results.json')
        try:
            with open(json_path, 'r') as file:
                camera_data = json.load(file)
            camera_data = [cam for cam in camera_data if cam['name_of_camera'] != camera['name_of_camera']]
            with open(json_path, 'w') as file:
                json.dump(camera_data, file, indent=4)
            print(f"Camera {camera['name_of_camera']} removed from 'camera_results.json'.")
        except Exception as e:
            print(f"Error removing camera from 'camera_results.json': {e}")

    def check_and_start_streams(self):
        json_path = os.path.join(os.path.dirname(__file__), 'camera_results.json')
        try:
            with open(json_path, 'r') as file:
                camera_data = json.load(file)
            for camera in camera_data:
                self.setup_camera_stream(camera['name_of_camera'])
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass
        except Exception as e:
            print(f"Error starting streams: {e}")

class CameraDiscoveryThread(QThread):
    progress = Signal(int)
    camera_found = Signal(dict)
    finished = Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.stop_event = asyncio.Event()

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        subnets = ["192.168.1.0/24", "192.168.2.0/24"]
        cameras = loop.run_until_complete(discover_cameras(subnets, self.progress, self.camera_found, self.stop_event))
        self.finished.emit(cameras)

    def stop(self):
        self.stop_event.set()

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"Error starting application: {e}")
        QMessageBox.critical(None, "Σφάλμα", f"Απροσδιόριστο σφάλμα κατά την εκκίνηση της εφαρμογής: {e}")
