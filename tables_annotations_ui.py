# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tables_annotations.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1276, 868)
        MainWindow.setStyleSheet(u"background-color: rgb(208, 212, 217);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 191, 21))
        self.label.setStyleSheet(u"font: 11pt \"Segoe UI\";")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(1090, 380, 181, 461))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_save_annotations = QPushButton(self.frame)
        self.pushButton_save_annotations.setObjectName(u"pushButton_save_annotations")
        self.pushButton_save_annotations.setEnabled(True)
        self.pushButton_save_annotations.setGeometry(QRect(10, 350, 161, 41))
        self.pushButton_save_annotations.setMouseTracking(True)
        self.pushButton_save_annotations.setTabletTracking(True)
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
        self.pushButton_save_annotations.setIconSize(QSize(33, 33))
        self.pushButton_save_annotations.setAutoDefault(True)
        self.pushButton_quit_annotations = QPushButton(self.frame)
        self.pushButton_quit_annotations.setObjectName(u"pushButton_quit_annotations")
        self.pushButton_quit_annotations.setEnabled(True)
        self.pushButton_quit_annotations.setGeometry(QRect(10, 400, 161, 41))
        self.pushButton_quit_annotations.setMouseTracking(True)
        self.pushButton_quit_annotations.setTabletTracking(True)
        self.pushButton_quit_annotations.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_quit_annotations.setIconSize(QSize(33, 33))
        self.pushButton_quit_annotations.setAutoDefault(True)
        self.pushButton_save_annotations_3 = QPushButton(self.frame)
        self.pushButton_save_annotations_3.setObjectName(u"pushButton_save_annotations_3")
        self.pushButton_save_annotations_3.setEnabled(True)
        self.pushButton_save_annotations_3.setGeometry(QRect(10, 40, 161, 41))
        self.pushButton_save_annotations_3.setMouseTracking(True)
        self.pushButton_save_annotations_3.setTabletTracking(True)
        self.pushButton_save_annotations_3.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_save_annotations_3.setIconSize(QSize(33, 33))
        self.pushButton_save_annotations_3.setAutoDefault(True)
        self.pushButton_save_annotations_4 = QPushButton(self.frame)
        self.pushButton_save_annotations_4.setObjectName(u"pushButton_save_annotations_4")
        self.pushButton_save_annotations_4.setEnabled(True)
        self.pushButton_save_annotations_4.setGeometry(QRect(10, 90, 161, 41))
        self.pushButton_save_annotations_4.setMouseTracking(True)
        self.pushButton_save_annotations_4.setTabletTracking(True)
        self.pushButton_save_annotations_4.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_save_annotations_4.setIconSize(QSize(33, 33))
        self.pushButton_save_annotations_4.setAutoDefault(True)
        self.pushButton_save_annotations_5 = QPushButton(self.frame)
        self.pushButton_save_annotations_5.setObjectName(u"pushButton_save_annotations_5")
        self.pushButton_save_annotations_5.setEnabled(True)
        self.pushButton_save_annotations_5.setGeometry(QRect(10, 140, 161, 41))
        self.pushButton_save_annotations_5.setMouseTracking(True)
        self.pushButton_save_annotations_5.setTabletTracking(True)
        self.pushButton_save_annotations_5.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_save_annotations_5.setIconSize(QSize(33, 33))
        self.pushButton_save_annotations_5.setAutoDefault(True)
        self.textEdit_log = QTextEdit(self.centralwidget)
        self.textEdit_log.setObjectName(u"textEdit_log")
        self.textEdit_log.setGeometry(QRect(750, 50, 341, 771))
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 80, 691, 461))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.graphicsView_image_annotations = QGraphicsView(self.frame_2)
        self.graphicsView_image_annotations.setObjectName(u"graphicsView_image_annotations")
        self.graphicsView_image_annotations.setGeometry(QRect(30, 40, 631, 391))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_image_annotations.sizePolicy().hasHeightForWidth())
        self.graphicsView_image_annotations.setSizePolicy(sizePolicy)
        self.graphicsView_image_annotations.setFrameShape(QFrame.Shape.NoFrame)
        self.graphicsView_image_annotations.setLineWidth(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushButton_save_annotations.setDefault(True)
        self.pushButton_quit_annotations.setDefault(True)
        self.pushButton_save_annotations_3.setDefault(True)
        self.pushButton_save_annotations_4.setDefault(True)
        self.pushButton_save_annotations_5.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Set Tables to Space", None))
#if QT_CONFIG(accessibility)
        self.pushButton_save_annotations.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.pushButton_save_annotations.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(accessibility)
        self.pushButton_quit_annotations.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.pushButton_quit_annotations.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(accessibility)
        self.pushButton_save_annotations_3.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.pushButton_save_annotations_3.setText(QCoreApplication.translate("MainWindow", u"Move", None))
#if QT_CONFIG(accessibility)
        self.pushButton_save_annotations_4.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.pushButton_save_annotations_4.setText(QCoreApplication.translate("MainWindow", u"Rotate", None))
#if QT_CONFIG(accessibility)
        self.pushButton_save_annotations_5.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.pushButton_save_annotations_5.setText(QCoreApplication.translate("MainWindow", u"Drag Corner", None))
    # retranslateUi

