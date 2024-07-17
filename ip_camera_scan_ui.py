# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ip_camera_scan.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QLabel,
    QLineEdit, QListView, QMainWindow, QProgressBar,
    QPushButton, QScrollBar, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1201, 884)
        MainWindow.setStyleSheet(u"\n"
"    QMainWindow {\n"
"      background-color: #F0F0F0;\n"
"    }\n"
"    QFrame {\n"
"      border-radius: 10px;\n"
"      background-color: #FFFFFF;\n"
"      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);\n"
"    }\n"
"    QPushButton {\n"
"      border: none;\n"
"      border-radius: 5px;\n"
"      padding: 10px 20px;\n"
"      color: #FFFFFF;\n"
"      background-color: #3A617F;\n"
"      transition: background-color 0.3s ease;\n"
"    }\n"
"    QPushButton:hover {\n"
"      background-color: #5A819F;\n"
"    }\n"
"    QLineEdit {\n"
"      border: 1px solid #CCCCCC;\n"
"      border-radius: 5px;\n"
"      padding: 5px;\n"
"    }\n"
"    QLabel {\n"
"      font-size: 14px;\n"
"      color: #333333;\n"
"    }\n"
"    QProgressBar {\n"
"      background-color: #E0E0E0;\n"
"      border-radius: 5px;\n"
"      text-align: center;\n"
"    }\n"
"    QProgressBar::chunk {\n"
"      background-color: #FF9C33;\n"
"      border-radius: 5px;\n"
"    }\n"
"    QListView {\n"
"      border: 1px solid #CCCCCC;\n"
"     "
                        " border-radius: 5px;\n"
"    }\n"
"   ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(270, 20, 831, 851))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.graphicsView_camera1 = QGraphicsView(self.frame)
        self.graphicsView_camera1.setObjectName(u"graphicsView_camera1")
        self.graphicsView_camera1.setGeometry(QRect(20, 20, 791, 401))
        self.graphicsView_camera1.setFrameShape(QFrame.Shape.Panel)
        self.graphicsView_camera1.setFrameShadow(QFrame.Shadow.Raised)
        self.graphicsView_camera2 = QGraphicsView(self.frame)
        self.graphicsView_camera2.setObjectName(u"graphicsView_camera2")
        self.graphicsView_camera2.setGeometry(QRect(20, 430, 791, 401))
        self.graphicsView_camera2.setFrameShape(QFrame.Shape.Box)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 370, 221, 161))
        self.frame_2.setFrameShape(QFrame.Shape.Panel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_username = QLineEdit(self.frame_2)
        self.lineEdit_username.setObjectName(u"lineEdit_username")
        self.lineEdit_username.setGeometry(QRect(10, 32, 191, 22))
        self.lineEdit_username.setStyleSheet(u"font: 7pt \"Segoe UI\";")
        self.lineEdit_password = QLineEdit(self.frame_2)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setGeometry(QRect(10, 60, 191, 22))
        self.lineEdit_password.setStyleSheet(u"font: 7pt \"Segoe UI\";")
        self.lineEdit_name_of_camera = QLineEdit(self.frame_2)
        self.lineEdit_name_of_camera.setObjectName(u"lineEdit_name_of_camera")
        self.lineEdit_name_of_camera.setGeometry(QRect(10, 88, 191, 22))
        self.lineEdit_name_of_camera.setStyleSheet(u"font: 7pt \"Segoe UI\";")
        self.label_add_new_camera = QLabel(self.frame_2)
        self.label_add_new_camera.setObjectName(u"label_add_new_camera")
        self.label_add_new_camera.setGeometry(QRect(10, 10, 131, 16))
        self.pushButton_add_camera = QPushButton(self.frame_2)
        self.pushButton_add_camera.setObjectName(u"pushButton_add_camera")
        self.pushButton_add_camera.setGeometry(QRect(70, 120, 75, 31))
        self.RenewIP = QPushButton(self.centralwidget)
        self.RenewIP.setObjectName(u"RenewIP")
        self.RenewIP.setGeometry(QRect(30, 290, 81, 41))
        self.RenewIP.setToolTipDuration(5)
        self.RenewIP.setStyleSheet(u"font: 7pt \"Segoe UI\";")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(30, 50, 221, 217))
        self.frame_3.setFrameShape(QFrame.Shape.WinPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.progressBar = QProgressBar(self.frame_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 190, 201, 10))
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setValue(0)
        self.listView_founded_names_of_cameras = QListView(self.frame_3)
        self.listView_founded_names_of_cameras.setObjectName(u"listView_founded_names_of_cameras")
        self.listView_founded_names_of_cameras.setGeometry(QRect(20, 10, 181, 167))
        self.listView_founded_names_of_cameras.setFrameShape(QFrame.Shape.NoFrame)
        self.Stop_searching_button = QPushButton(self.centralwidget)
        self.Stop_searching_button.setObjectName(u"Stop_searching_button")
        self.Stop_searching_button.setGeometry(QRect(190, 290, 61, 41))
        self.Stop_searching_button.setToolTipDuration(5)
        self.Stop_searching_button.setStyleSheet(u"background-color: rgb(255, 32, 16);\n"
"font: 7pt \"Segoe UI\";")
        self.horizontalScrollBar_snapshot_timer = QScrollBar(self.centralwidget)
        self.horizontalScrollBar_snapshot_timer.setObjectName(u"horizontalScrollBar_snapshot_timer")
        self.horizontalScrollBar_snapshot_timer.setGeometry(QRect(60, 660, 160, 16))
        self.horizontalScrollBar_snapshot_timer.setMaximum(15)
        self.horizontalScrollBar_snapshot_timer.setSliderPosition(0)
        self.horizontalScrollBar_snapshot_timer.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalScrollBar_snapshot_timer.setInvertedControls(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_name_of_camera.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Camera Name", None))
        self.label_add_new_camera.setText(QCoreApplication.translate("MainWindow", u"Add a new camera", None))
        self.pushButton_add_camera.setText(QCoreApplication.translate("MainWindow", u"Add", None))
#if QT_CONFIG(tooltip)
        self.RenewIP.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.RenewIP.setText(QCoreApplication.translate("MainWindow", u"Renew IP", None))
#if QT_CONFIG(tooltip)
        self.Stop_searching_button.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Stop_searching_button.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
    # retranslateUi

