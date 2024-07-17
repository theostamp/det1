# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reservation.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCalendarWidget, QFrame,
    QGraphicsView, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTimeEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1524, 847)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 1521, 831))
        self.frame.setStyleSheet(u"\n"
"       background-color: #e6e6e6; /* \u0395\u03bb\u03b1\u03c6\u03c1\u03ce\u03c2 \u03b1\u03bd\u03bf\u03b9\u03c7\u03c4\u03cc\u03c4\u03b5\u03c1\u03bf \u03b3\u03ba\u03c1\u03b9 */\n"
"       border-radius: 15px; /* \u03a3\u03c4\u03c1\u03bf\u03b3\u03b3\u03c5\u03bb\u03b5\u03bc\u03ad\u03bd\u03b5\u03c2 \u03b3\u03c9\u03bd\u03af\u03b5\u03c2 */\n"
"     ")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.calendarWidget = QCalendarWidget(self.frame)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(20, 40, 551, 361))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setMouseTracking(True)
        self.calendarWidget.setTabletTracking(True)
        self.calendarWidget.setAcceptDrops(True)
        self.calendarWidget.setAutoFillBackground(False)
        self.calendarWidget.setStyleSheet(u"\n"
"        color: #236b71; /* \u03a3\u03ba\u03bf\u03cd\u03c1\u03bf \u03bc\u03c0\u03bb\u03b5-\u03c0\u03c1\u03ac\u03c3\u03b9\u03bd\u03bf */\n"
"        selection-background-color: #ff4000; /* \u0388\u03bd\u03c4\u03bf\u03bd\u03bf \u03ba\u03cc\u03ba\u03ba\u03b9\u03bd\u03bf */\n"
"        alternate-background-color: #ffffff; /* \u039b\u03b5\u03c5\u03ba\u03cc */\n"
"        background-color: #f0f0f0; /* \u0395\u03bb\u03b1\u03c6\u03c1\u03ce\u03c2 \u03b1\u03bd\u03bf\u03b9\u03c7\u03c4\u03cc \u03b3\u03ba\u03c1\u03b9 */\n"
"      ")
        self.calendarWidget.setGridVisible(True)
        self.booking_area = QGroupBox(self.frame)
        self.booking_area.setObjectName(u"booking_area")
        self.booking_area.setGeometry(QRect(20, 430, 551, 341))
        font1 = QFont()
        font1.setPointSize(11)
        self.booking_area.setFont(font1)
        self.booking_area.setMouseTracking(True)
        self.booking_area.setTabletTracking(True)
        self.booking_area.setAcceptDrops(True)
        self.booking_area.setAutoFillBackground(False)
        self.booking_area.setStyleSheet(u"\n"
"        background-color: #ffffff; /* \u039b\u03b5\u03c5\u03ba\u03cc \u03b3\u03b9\u03b1 \u03ba\u03b1\u03b8\u03b1\u03c1\u03ae \u03b5\u03bc\u03c6\u03ac\u03bd\u03b9\u03c3\u03b7 */\n"
"        border: 1px solid #d3d3d3; /* \u0391\u03bd\u03bf\u03b9\u03c7\u03c4\u03cc \u03b3\u03ba\u03c1\u03b9 \u03c0\u03b5\u03c1\u03af\u03b3\u03c1\u03b1\u03bc\u03bc\u03b1 */\n"
"        border-radius: 10px; /* \u03a3\u03c4\u03c1\u03bf\u03b3\u03b3\u03c5\u03bb\u03b5\u03bc\u03ad\u03bd\u03b5\u03c2 \u03b3\u03c9\u03bd\u03af\u03b5\u03c2 */\n"
"      ")
        self.booking_area.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.booking_area.setFlat(False)
        self.booking_area.setCheckable(False)
        self.bookingButton = QPushButton(self.booking_area)
        self.bookingButton.setObjectName(u"bookingButton")
        self.bookingButton.setGeometry(QRect(360, 30, 171, 71))
        self.bookingButton.setStyleSheet(u"\n"
"         QPushButton {\n"
"             color: #ffffff;\n"
"             border-radius: 10px;\n"
"             background-color: #3f718c;\n"
"             border: 1px solid #ff9500; /* \u03a0\u03c1\u03bf\u03c3\u03b8\u03ae\u03ba\u03b7 \u03c0\u03bf\u03c1\u03c4\u03bf\u03ba\u03b1\u03bb\u03af \u03c0\u03b5\u03c1\u03b9\u03b3\u03c1\u03ac\u03bc\u03bc\u03b1\u03c4\u03bf\u03c2 */\n"
"         }\n"
"         QPushButton:hover {\n"
"             background-color: #636363;\n"
"         }\n"
"       ")
        self.cancelReservationButton = QPushButton(self.booking_area)
        self.cancelReservationButton.setObjectName(u"cancelReservationButton")
        self.cancelReservationButton.setGeometry(QRect(360, 120, 171, 71))
        self.cancelReservationButton.setStyleSheet(u"\n"
"         QPushButton {\n"
"             color: #ffffff;\n"
"             border-radius: 10px;\n"
"             background-color: #3f718c;\n"
"             border: 1px solid #ff9500; /* \u03a0\u03c1\u03bf\u03c3\u03b8\u03ae\u03ba\u03b7 \u03c0\u03bf\u03c1\u03c4\u03bf\u03ba\u03b1\u03bb\u03af \u03c0\u03b5\u03c1\u03b9\u03b3\u03c1\u03ac\u03bc\u03bc\u03b1\u03c4\u03bf\u03c2 */\n"
"         }\n"
"         QPushButton:hover {\n"
"             background-color: #636363;\n"
"         }\n"
"       ")
        self.timeEdit_book = QTimeEdit(self.booking_area)
        self.timeEdit_book.setObjectName(u"timeEdit_book")
        self.timeEdit_book.setGeometry(QRect(160, 230, 151, 41))
        self.timeEdit_book.setStyleSheet(u"\n"
"         background-color: #ffffff;\n"
"         font: 12pt \"Segoe UI\";\n"
"         border: 1px solid #d3d3d3;\n"
"         border-radius: 5px;\n"
"       ")
        self.frame_4 = QFrame(self.booking_area)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(160, 40, 153, 151))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_nameBook = QLineEdit(self.frame_4)
        self.lineEdit_nameBook.setObjectName(u"lineEdit_nameBook")
        self.lineEdit_nameBook.setGeometry(QRect(10, 0, 133, 41))
        self.lineEdit_nameBook.setStyleSheet(u"\n"
"          background-color: #ffffff;\n"
"          font: italic 10pt \"Segoe UI\";\n"
"          border: 1px solid #d3d3d3;\n"
"          border-radius: 5px;\n"
"        ")
        self.lineEdit_phoneBook = QLineEdit(self.frame_4)
        self.lineEdit_phoneBook.setObjectName(u"lineEdit_phoneBook")
        self.lineEdit_phoneBook.setGeometry(QRect(10, 50, 133, 41))
        self.lineEdit_phoneBook.setStyleSheet(u"\n"
"          background-color: #ffffff;\n"
"          font: italic 10pt \"Segoe UI\";\n"
"          border: 1px solid #d3d3d3;\n"
"          border-radius: 5px;\n"
"        ")
        self.lineEdit_tableBook = QLineEdit(self.frame_4)
        self.lineEdit_tableBook.setObjectName(u"lineEdit_tableBook")
        self.lineEdit_tableBook.setGeometry(QRect(10, 100, 133, 41))
        self.lineEdit_tableBook.setStyleSheet(u"\n"
"          background-color: #ffffff;\n"
"          font: italic 10pt \"Segoe UI\";\n"
"          border: 1px solid #d3d3d3;\n"
"          border-radius: 5px;\n"
"        ")
        self.label = QLabel(self.booking_area)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 50, 61, 21))
        self.label_2 = QLabel(self.booking_area)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 150, 51, 21))
        self.label_3 = QLabel(self.booking_area)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 100, 51, 21))
        self.graphicsView_reserve = QGraphicsView(self.frame)
        self.graphicsView_reserve.setObjectName(u"graphicsView_reserve")
        self.graphicsView_reserve.setEnabled(True)
        self.graphicsView_reserve.setGeometry(QRect(600, 50, 871, 731))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_reserve.sizePolicy().hasHeightForWidth())
        self.graphicsView_reserve.setSizePolicy(sizePolicy)
        self.graphicsView_reserve.setMinimumSize(QSize(10, 10))
        self.graphicsView_reserve.setMaximumSize(QSize(16777215, 16777215))
        self.graphicsView_reserve.setMouseTracking(True)
        self.graphicsView_reserve.setTabletTracking(True)
        self.graphicsView_reserve.setAutoFillBackground(True)
        self.graphicsView_reserve.setStyleSheet(u"\n"
"        color: #cacaca;\n"
"        background-color: #f0f0f0;\n"
"        border: 1px solid #d3d3d3;\n"
"        border-radius: 5px;\n"
"      ")
        self.graphicsView_reserve.setFrameShape(QFrame.Shape.Box)
        self.graphicsView_reserve.setFrameShadow(QFrame.Shadow.Raised)
        self.graphicsView_reserve.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.booking_area.setTitle(QCoreApplication.translate("MainWindow", u"Booking", None))
        self.bookingButton.setText(QCoreApplication.translate("MainWindow", u"Set Reservation", None))
        self.cancelReservationButton.setText(QCoreApplication.translate("MainWindow", u"Cancel Reservation", None))
        self.lineEdit_nameBook.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.lineEdit_phoneBook.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.lineEdit_tableBook.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Table", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Table", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Phone", None))
    # retranslateUi

