# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'annotation.ui'
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1292, 810)
        MainWindow.setStyleSheet(u"background-color: rgb(209, 209, 209);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(210, 50, 981, 591))
        self.pushButton_load_image = QPushButton(self.centralwidget)
        self.pushButton_load_image.setObjectName(u"pushButton_load_image")
        self.pushButton_load_image.setGeometry(QRect(60, 60, 121, 71))
        self.pushButton_load_image.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_save_annotations = QPushButton(self.centralwidget)
        self.pushButton_save_annotations.setObjectName(u"pushButton_save_annotations")
        self.pushButton_save_annotations.setGeometry(QRect(60, 160, 121, 71))
        self.pushButton_save_annotations.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_delete_rest = QPushButton(self.centralwidget)
        self.pushButton_delete_rest.setObjectName(u"pushButton_delete_rest")
        self.pushButton_delete_rest.setGeometry(QRect(610, 680, 121, 51))
        self.pushButton_delete_rest.setStyleSheet(u"QPushButton {\n"
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_load_image.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.pushButton_save_annotations.setText(QCoreApplication.translate("MainWindow", u"Save Annotations", None))
        self.pushButton_delete_rest.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
    # retranslateUi

