# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'waiters.ui'
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
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(929, 715)
        MainWindow.setStyleSheet(u"\n"
"   QMainWindow {\n"
"      background-color: rgb(214, 214, 214);\n"
"   }\n"
"   QFrame {\n"
"      border-radius: 10px;\n"
"      background-color: #FFFFFF;\n"
"      border: 1px solid #DDDDDD;\n"
"      padding: 10px;\n"
"   }\n"
"   QPushButton {\n"
"      color: #FFFFFF;\n"
"      border-radius: 10px;\n"
"      font: 10pt \"Segoe UI\";\n"
"      background-color: #3F718C;\n"
"      border: none;\n"
"      padding: 10px;\n"
"      margin: 5px;\n"
"   }\n"
"   QPushButton:hover {\n"
"      background-color: #5A819F;\n"
"   }\n"
"   QLineEdit {\n"
"      background-color: #FFFFFF;\n"
"      font: italic 10pt \"Segoe UI\";\n"
"      border: 1px solid #CCCCCC;\n"
"      border-radius: 5px;\n"
"      padding: 5px;\n"
"      margin: 5px;\n"
"   }\n"
"   QLabel {\n"
"      color: #447781;\n"
"      font: 12pt \"Segoe UI\";\n"
"   }\n"
"   QListView {\n"
"      border: 1px solid #CCCCCC;\n"
"      border-radius: 5px;\n"
"   }\n"
"   ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 20, 351, 261))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(30, 10, 291, 231))
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Plain)
        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 40, 231, 41))
        self.lineEdit.setMouseTracking(False)
        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(30, 80, 231, 41))
#if QT_CONFIG(accessibility)
        self.lineEdit_2.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_3 = QLineEdit(self.frame_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(30, 120, 231, 41))
        self.lineEdit_3.setClearButtonEnabled(True)
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 170, 131, 51))
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, -10, 131, 41))
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 310, 351, 371))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.listView_waiters = QListView(self.frame_2)
        self.listView_waiters.setObjectName(u"listView_waiters")
        self.listView_waiters.setGeometry(QRect(10, 10, 331, 351))
        self.listView_waiters.setFrameShape(QFrame.Shape.Panel)
        self.QrPlaceholder = QLabel(self.centralwidget)
        self.QrPlaceholder.setObjectName(u"QrPlaceholder")
        self.QrPlaceholder.setGeometry(QRect(440, 150, 421, 341))
        self.QrPlaceholder.setFrameShape(QFrame.Shape.NoFrame)
        self.pushButton_delete_waiter = QPushButton(self.centralwidget)
        self.pushButton_delete_waiter.setObjectName(u"pushButton_delete_waiter")
        self.pushButton_delete_waiter.setGeometry(QRect(590, 510, 141, 51))
        self.Waiter_name = QLabel(self.centralwidget)
        self.Waiter_name.setObjectName(u"Waiter_name")
        self.Waiter_name.setGeometry(QRect(560, 90, 181, 41))
        self.Waiter_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Surname", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NickName", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Create Waiter QR", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Register Waiter", None))
        self.QrPlaceholder.setText("")
        self.pushButton_delete_waiter.setText(QCoreApplication.translate("MainWindow", u"Delete ", None))
        self.Waiter_name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
    # retranslateUi

