# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(685, 502)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 1111, 721))
        self.widget.setStyleSheet(u"\n"
"QPushButton {\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"	font: 500 9pt \"Quicksand Medium\";\n"
"    background-color: blue;\n"
"    border: none;\n"
"    padding: 10px;\n"
"    margin: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5A819F;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    color: rgb(255, 195, 99);\n"
"\n"
"font: 500 9pt \"Quicksand Medium\";\n"
"   	color: black;\n"
"    margin: 5px;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #447781;\n"
"font: 500 9pt \"Quicksand Medium\";\n"
"}\n"
"\n"
"QFrame {\n"
"    border-radius: 10px;\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #DDDDDD;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(50, 40, 571, 271))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 170, 201, 51))
        self.pushButton.setStyleSheet(u"background-color: rgb(19, 113, 172);")
        self.pushButton.setFlat(False)
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(160, 90, 261, 51))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QSize(200, 40))
        self.lineEdit.setStyleSheet(u"")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(74, 90, 481, 51))
        self.label.setStyleSheet(u"")
        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(160, 30, 261, 51))
        self.lineEdit_2.setMinimumSize(QSize(200, 40))
        self.lineEdit_2.setStyleSheet(u"")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(74, 30, 481, 51))
        self.label_2.setStyleSheet(u"")
        self.label_2.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 340, 571, 51))
        self.label_3.setStyleSheet(u"")
        self.register_button = QPushButton(self.widget)
        self.register_button.setObjectName(u"register_button")
        self.register_button.setGeometry(QRect(250, 340, 201, 51))
        self.register_button.setStyleSheet(u"background-color: rgb(19, 113, 172);")
        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-20, 320, 1101, 5))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"login", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insert your PassWord", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PassWord", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insert your UserName", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"UserName", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"New Account", None))
        self.register_button.setText(QCoreApplication.translate("MainWindow", u"Register", None))
    # retranslateUi

