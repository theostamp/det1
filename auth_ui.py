# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 801, 601))
        self.frame.setStyleSheet(u"background-color: rgb(191, 191, 191);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setLineWidth(-2)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(200, 400, 421, 171))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.PushButton_google_login = QPushButton(self.frame_2)
        self.PushButton_google_login.setObjectName(u"PushButton_google_login")
        self.PushButton_google_login.setGeometry(QRect(10, 7, 401, 61))
        font = QFont()
        font.setPointSize(12)
        self.PushButton_google_login.setFont(font)
        self.PushButton_google_login.setAutoFillBackground(False)
        self.PushButton_google_login.setStyleSheet(u"background-color: rgb(243, 243, 243);")
        self.PushButton_google_login.setCheckable(False)
        self.PushButton_google_login.setAutoDefault(False)
        self.PushButton_google_login.setFlat(False)
        self.PushButton_microsoft_login = QPushButton(self.frame_2)
        self.PushButton_microsoft_login.setObjectName(u"PushButton_microsoft_login")
        self.PushButton_microsoft_login.setGeometry(QRect(10, 81, 401, 61))
        self.PushButton_microsoft_login.setFont(font)
        self.PushButton_microsoft_login.setAutoFillBackground(False)
        self.PushButton_microsoft_login.setStyleSheet(u"background-color: rgb(243, 243, 243);")
        self.PushButton_microsoft_login.setCheckable(False)
        self.PushButton_microsoft_login.setAutoDefault(False)
        self.PushButton_microsoft_login.setFlat(False)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(180, 120, 431, 271))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.lineEdit_username = QLineEdit(self.frame_3)
        self.lineEdit_username.setObjectName(u"lineEdit_username")
        self.lineEdit_username.setGeometry(QRect(40, 10, 361, 51))
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 60, 121, 31))
        self.lineEdit_password = QLineEdit(self.frame_3)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setGeometry(QRect(40, 110, 361, 51))
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 170, 121, 31))
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 240, 181, 21))
        self.label_3.setStyleSheet(u"color: rgb(25, 79, 255);")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(180, 20, 431, 80))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 20, 171, 41))
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(240, 20, 171, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.PushButton_google_login.setDefault(False)
        self.PushButton_microsoft_login.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.PushButton_google_login.setText(QCoreApplication.translate("MainWindow", u"login with Google", None))
        self.PushButton_microsoft_login.setText(QCoreApplication.translate("MainWindow", u"login with Microsoft", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"e-mail", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"forgot your password?", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"login", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"signin", None))
    # retranslateUi

