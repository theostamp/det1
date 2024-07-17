# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stats.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1102, 874)
        MainWindow.setStyleSheet(u"font: 500 10pt \"Quicksand Medium\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.daily = QFrame(self.centralwidget)
        self.daily.setObjectName(u"daily")
        self.daily.setGeometry(QRect(60, 80, 431, 331))
        self.daily.setFrameShape(QFrame.Shape.StyledPanel)
        self.daily.setFrameShadow(QFrame.Shadow.Raised)
        self.monthly = QFrame(self.centralwidget)
        self.monthly.setObjectName(u"monthly")
        self.monthly.setGeometry(QRect(60, 480, 431, 321))
        self.monthly.setFrameShape(QFrame.Shape.StyledPanel)
        self.monthly.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 50, 121, 21))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 450, 161, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1102, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Daily Statitics", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Monthly  Statistics", None))
    # retranslateUi

