# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scan_camera.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QLineEdit,
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1389, 874)
        MainWindow.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 200, 581, 291))
        self.frame_2.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.listView_ips = QListView(self.frame_2)
        self.listView_ips.setObjectName(u"listView_ips")
        self.listView_ips.setGeometry(QRect(20, 20, 541, 251))
        self.graphicsView_1 = QGraphicsView(self.centralwidget)
        self.graphicsView_1.setObjectName(u"graphicsView_1")
        self.graphicsView_1.setGeometry(QRect(620, 60, 741, 431))
        self.graphicsView_1.setFrameShape(QFrame.Panel)
        self.graphicsView_1.setFrameShadow(QFrame.Sunken)
        self.graphicsView_1.setLineWidth(1)
        self.graphicsView_1.setMidLineWidth(2)
        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 60, 581, 131))
        self.frame_5.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.pushButton_search_camera = QPushButton(self.frame_5)
        self.pushButton_search_camera.setObjectName(u"pushButton_search_camera")
        self.pushButton_search_camera.setGeometry(QRect(320, 40, 151, 51))
        self.pushButton_search_camera.setStyleSheet(u"QPushButton {\n"
"    color: rgb(249, 249, 249);\n"
"    border-radius: 0px;\n"
"	\n"
"	\n"
"	background-color: rgb(63, 113, 140);\n"
"	\n"
"    border-right: 15px solid orange; /* \u03a0\u03c1\u03bf\u03c3\u03b8\u03ae\u03ba\u03b7 \u03ba\u03af\u03c4\u03c1\u03b9\u03bd\u03b7\u03c2 \u03b3\u03c1\u03b1\u03bc\u03bc\u03ae\u03c2 \u03c0\u03b5\u03c1\u03b9\u03b3\u03c1\u03ac\u03bc\u03bc\u03b1\u03c4\u03bf\u03c2 \u03c3\u03c4\u03b7 \u03b4\u03b5\u03be\u03b9\u03ac \u03c0\u03bb\u03b5\u03c5\u03c1\u03ac */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   \n"
"	background-color: rgb(99, 99, 99);\n"
"}\n"
"")
        self.lineEdit_password = QLineEdit(self.frame_5)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setGeometry(QRect(10, 70, 201, 41))
        self.lineEdit_password.setTabletTracking(True)
        self.lineEdit_password.setAutoFillBackground(False)
        self.lineEdit_password.setStyleSheet(u"background-color: rgb(236, 236, 236);\n"
"font: italic 10pt \"Segoe UI\";")
        self.lineEdit_password.setFrame(False)
        self.lineEdit_password.setAlignment(Qt.AlignCenter)
        self.lineEdit_username = QLineEdit(self.frame_5)
        self.lineEdit_username.setObjectName(u"lineEdit_username")
        self.lineEdit_username.setGeometry(QRect(10, 20, 201, 41))
        self.lineEdit_username.setTabletTracking(True)
        self.lineEdit_username.setAutoFillBackground(False)
        self.lineEdit_username.setStyleSheet(u"background-color: rgb(236, 236, 236);\n"
"font: italic 10pt \"Segoe UI\";")
        self.lineEdit_username.setFrame(False)
        self.lineEdit_username.setAlignment(Qt.AlignCenter)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 530, 671, 331))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.listView_onvif = QListView(self.frame)
        self.listView_onvif.setObjectName(u"listView_onvif")
        self.listView_onvif.setGeometry(QRect(20, 0, 631, 321))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_search_camera.setText(QCoreApplication.translate("MainWindow", u" Search IP Camera", None))
        self.lineEdit_password.setInputMask("")
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_username.setInputMask("")
        self.lineEdit_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
    # retranslateUi

