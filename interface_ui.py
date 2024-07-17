# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QAbstractSpinBox, QApplication,
    QDoubleSpinBox, QFrame, QGraphicsView, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QListView, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QTabWidget,
    QTableWidget, QTableWidgetItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1926, 1017)
        MainWindow.setMouseTracking(True)
        MainWindow.setTabletTracking(True)
        MainWindow.setAcceptDrops(True)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet(u"")
        MainWindow.setInputMethodHints(Qt.InputMethodHint.ImhMultiLine)
        MainWindow.setDocumentMode(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setTabletTracking(True)
        self.centralwidget.setAcceptDrops(True)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"background-color: rgb(208, 212, 217);")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(1011, 601))
        self.frame.setStyleSheet(u"background-color: rgb(208, 212, 217);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.order = QTabWidget(self.frame)
        self.order.setObjectName(u"order")
        self.order.setEnabled(True)
        self.order.setGeometry(QRect(220, -10, 1681, 1041))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.order.sizePolicy().hasHeightForWidth())
        self.order.setSizePolicy(sizePolicy)
        self.order.setMouseTracking(True)
        self.order.setTabletTracking(True)
        self.order.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.order.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.order.setAcceptDrops(True)
        self.order.setAutoFillBackground(False)
        self.order.setStyleSheet(u"     QTabWidget::pane {\n"
"	\n"
"           \n"
"                background: #f0f0f0;\n"
"            }\n"
"            QTabBar::tab {\n"
"                background: #e0e0e0;\n"
"				font: 500 11pt \"Quicksand Medium\";\n"
"              \n"
"                padding: 15px;\n"
"                margin: 8px;\n"
"                min-width: 100px;\n"
"            }\n"
"            QTabBar::tab:selected {\n"
"\n"
"	background-color: rgb(130, 130, 130);\n"
"	color: rgb(255, 255, 255);\n"
"            \n"
"            }\n"
"            QTabBar::tab:hover {\n"
"                background: #c0c0c0;\n"
"            }")
        self.order.setTabPosition(QTabWidget.TabPosition.North)
        self.order.setTabShape(QTabWidget.TabShape.Rounded)
        self.order.setIconSize(QSize(42, 30))
        self.order.setElideMode(Qt.TextElideMode.ElideMiddle)
        self.order.setUsesScrollButtons(True)
        self.order.setDocumentMode(True)
        self.order.setTabsClosable(False)
        self.order.setMovable(True)
        self.order.setTabBarAutoHide(False)
        self.tab_overview = QWidget()
        self.tab_overview.setObjectName(u"tab_overview")
        self.tab_overview.setEnabled(True)
        self.tab_overview.setMouseTracking(True)
        self.tab_overview.setTabletTracking(True)
        self.tab_overview.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.tab_overview.setAcceptDrops(True)
        self.tab_overview.setAutoFillBackground(False)
        self.frame_28 = QFrame(self.tab_overview)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setGeometry(QRect(-10, -50, 1331, 931))
        self.frame_28.setAutoFillBackground(False)
        self.frame_28.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Shadow.Plain)
        self.webEngineView_3 = QWebEngineView(self.frame_28)
        self.webEngineView_3.setObjectName(u"webEngineView_3")
        self.webEngineView_3.setEnabled(True)
        self.webEngineView_3.setGeometry(QRect(20, 89, 1291, 831))
        self.webEngineView_3.setAutoFillBackground(False)
        self.webEngineView_3.setStyleSheet(u"background-color: rgb(208, 212, 217);")
        self.webEngineView_3.setProperty("url", QUrl(u"about:blank"))
        self.frame_5 = QFrame(self.tab_overview)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(1380, -10, 281, 831))
        self.frame_5.setAutoFillBackground(False)
        self.frame_5.setStyleSheet(u"color: rgb(255, 195, 99);\n"
"font: 8pt \"Segoe UI\";\n"
"background-color: rgb(190, 190, 190);")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Plain)
        self.tableView = QTableWidget(self.frame_5)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(0, 80, 251, 491))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.tableView.setFont(font)
        self.tableView.setMouseTracking(True)
        self.tableView.setAutoFillBackground(False)
        self.tableView.setStyleSheet(u"background-color: rgb(190, 190, 190);\n"
"font: 11pt \"Segoe UI\";\n"
"color: rgb(49, 49, 49);\n"
"selection-color: rgb(255, 255, 255);")
        self.tableView.setFrameShape(QFrame.Shape.NoFrame)
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableView.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableView.setAutoScroll(False)
        self.tableView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableView.setProperty("showDropIndicator", False)
        self.tableView.setGridStyle(Qt.PenStyle.DotLine)
        self.tableView.setSortingEnabled(True)
        self.tableView.horizontalHeader().setVisible(True)
        self.tableView.horizontalHeader().setCascadingSectionResizes(False)
        self.tableView.horizontalHeader().setMinimumSectionSize(22)
        self.tableView.horizontalHeader().setHighlightSections(True)
        self.tableView.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.verticalHeader().setMinimumSectionSize(32)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 30, 131, 16))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(10)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setStyleSheet(u"color: rgb(44, 18, 3);")
        self.label_3.setScaledContents(True)
        self.frame_26 = QFrame(self.frame_5)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setGeometry(QRect(70, 710, 141, 81))
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.label_4 = QLabel(self.frame_26)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 30, 51, 21))
        self.label_4.setStyleSheet(u"color: rgb(44, 18, 3);")
        self.spinBox_notify_minutes = QSpinBox(self.frame_26)
        self.spinBox_notify_minutes.setObjectName(u"spinBox_notify_minutes")
        self.spinBox_notify_minutes.setGeometry(QRect(70, 30, 42, 22))
        self.spinBox_notify_minutes.setStyleSheet(u"color: rgb(44, 18, 3);\n"
"font: 12pt \"Segoe UI\";")
        self.label_5 = QLabel(self.frame_26)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(120, 30, 21, 21))
        self.label_5.setStyleSheet(u"color: rgb(44, 18, 3);")
        self.frame_20 = QFrame(self.frame_5)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(50, 620, 181, 81))
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.reset_occupation_time = QPushButton(self.frame_20)
        self.reset_occupation_time.setObjectName(u"reset_occupation_time")
        self.reset_occupation_time.setGeometry(QRect(10, 10, 161, 51))
        self.reset_occupation_time.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(2, 86, 213);\n"
"    color: rgb(249, 249, 249);\n"
"    border-radius:10px;\n"
"	height: 65px;\n"
"\n"
"	\n"
"    border-right: 15px solid blue /* \u03a0\u03c1\u03bf\u03c3\u03b8\u03ae\u03ba\u03b7 \u03ba\u03af\u03c4\u03c1\u03b9\u03bd\u03b7\u03c2 \u03b3\u03c1\u03b1\u03bc\u03bc\u03ae\u03c2 \u03c0\u03b5\u03c1\u03b9\u03b3\u03c1\u03ac\u03bc\u03bc\u03b1\u03c4\u03bf\u03c2 \u03c3\u03c4\u03b7 \u03b4\u03b5\u03be\u03b9\u03ac \u03c0\u03bb\u03b5\u03c5\u03c1\u03ac */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   \n"
"	background-color: rgb(99, 99, 99);\n"
"}\n"
"")
        self.line_6 = QFrame(self.frame_5)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(10, 60, 261, 16))
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_7 = QFrame(self.frame_5)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(10, 580, 261, 16))
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_8 = QFrame(self.tab_overview)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(1350, 0, 20, 821))
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)
        self.order.addTab(self.tab_overview, "")
        self.order_tab = QWidget()
        self.order_tab.setObjectName(u"order_tab")
        self.order_tab.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.order_tab.sizePolicy().hasHeightForWidth())
        self.order_tab.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        self.order_tab.setFont(font1)
        self.order_tab.setMouseTracking(True)
        self.order_tab.setTabletTracking(True)
        self.order_tab.setAcceptDrops(True)
        self.order_tab.setAutoFillBackground(False)
        self.label_21 = QLabel(self.order_tab)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(1340, 10, 111, 16))
        sizePolicy2.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy2)
        self.label_21.setStyleSheet(u"color: rgb(185, 86, 15);\n"
"font: 9pt \"Segoe UI\";")
        self.label_21.setScaledContents(True)
        self.label_17 = QLabel(self.order_tab)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(260, 0, 91, 31))
        sizePolicy2.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy2)
        self.label_17.setStyleSheet(u"color: rgb(185, 86, 15);\n"
"font: 9pt \"Segoe UI\";")
        self.label_17.setScaledContents(True)
        self.label_table_feat = QLabel(self.order_tab)
        self.label_table_feat.setObjectName(u"label_table_feat")
        self.label_table_feat.setGeometry(QRect(1180, 740, 451, 41))
        self.label_table_feat.setStyleSheet(u"color: rgb(45, 89, 93);\n"
"font: 14pt \"Segoe UI\";")
        self.label_table_feat.setFrameShape(QFrame.Shape.Panel)
        self.label_table_feat.setFrameShadow(QFrame.Shadow.Raised)
        self.webEngineView_2 = QWebEngineView(self.order_tab)
        self.webEngineView_2.setObjectName(u"webEngineView_2")
        self.webEngineView_2.setGeometry(QRect(20, 40, 601, 741))
        self.webEngineView_2.setProperty("url", QUrl(u"about:blank"))
        self.tableWidget_ord = QTableWidget(self.order_tab)
        self.tableWidget_ord.setObjectName(u"tableWidget_ord")
        self.tableWidget_ord.setGeometry(QRect(1190, 60, 431, 661))
        self.tableWidget_ord.setMouseTracking(True)
        self.tableWidget_ord.setTabletTracking(True)
        self.tableWidget_ord.setStyleSheet(u"font: 10pt \"Tahoma\";\n"
"\n"
"color: rgb(12, 12, 12);")
        self.tableWidget_ord.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget_ord.setFrameShadow(QFrame.Shadow.Raised)
        self.tableWidget_ord.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableWidget_ord.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_ord.setAutoScrollMargin(0)
        self.tableWidget_ord.setDragDropOverwriteMode(False)
        self.tableWidget_ord.setAlternatingRowColors(False)
        self.tableWidget_ord.setShowGrid(True)
        self.tableWidget_ord.setGridStyle(Qt.PenStyle.DotLine)
        self.tableWidget_ord.setCornerButtonEnabled(True)
        self.tableWidget_ord.setRowCount(0)
        self.tableWidget_ord.setColumnCount(0)
        self.tableWidget_ord.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_ord.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget_ord.horizontalHeader().setDefaultSectionSize(109)
        self.tableWidget_ord.horizontalHeader().setHighlightSections(True)
        self.tableWidget_ord.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_ord.verticalHeader().setVisible(True)
        self.tableWidget_ord.verticalHeader().setCascadingSectionResizes(True)
        self.label_22 = QLabel(self.order_tab)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(720, 10, 131, 20))
        sizePolicy2.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy2)
        self.label_22.setStyleSheet(u"color: rgb(185, 86, 15);\n"
"font: 9pt \"Segoe UI\";")
        self.label_22.setScaledContents(True)
        self.pushButton_deleteOrder = QPushButton(self.order_tab)
        self.pushButton_deleteOrder.setObjectName(u"pushButton_deleteOrder")
        self.pushButton_deleteOrder.setGeometry(QRect(1490, 790, 141, 51))
        self.pushButton_deleteOrder.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(2, 86, 213);\n"
"    color: rgb(249, 249, 249);\n"
"    border-radius:10px;\n"
"	height: 65px;\n"
"\n"
"    border-right: 15px solid blue /* \u03a0\u03c1\u03bf\u03c3\u03b8\u03ae\u03ba\u03b7 \u03ba\u03af\u03c4\u03c1\u03b9\u03bd\u03b7\u03c2 \u03b3\u03c1\u03b1\u03bc\u03bc\u03ae\u03c2 \u03c0\u03b5\u03c1\u03b9\u03b3\u03c1\u03ac\u03bc\u03bc\u03b1\u03c4\u03bf\u03c2 \u03c3\u03c4\u03b7 \u03b4\u03b5\u03be\u03b9\u03ac \u03c0\u03bb\u03b5\u03c5\u03c1\u03ac */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   \n"
"	background-color: rgb(99, 99, 99);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"../../.designer/.designer/.designer/backup/icons/cross-svgrepo-com.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_deleteOrder.setIcon(icon)
        self.pushButton_deleteOrder.setIconSize(QSize(28, 28))
        self.pushButton_printOrder = QPushButton(self.order_tab)
        self.pushButton_printOrder.setObjectName(u"pushButton_printOrder")
        self.pushButton_printOrder.setGeometry(QRect(1190, 790, 141, 51))
        self.pushButton_printOrder.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(2, 86, 213);\n"
"    color: rgb(249, 249, 249);\n"
"    border-radius:10px;\n"
"	height: 65px;\n"
"\n"
"    border-right: 15px solid blue /* \u03a0\u03c1\u03bf\u03c3\u03b8\u03ae\u03ba\u03b7 \u03ba\u03af\u03c4\u03c1\u03b9\u03bd\u03b7\u03c2 \u03b3\u03c1\u03b1\u03bc\u03bc\u03ae\u03c2 \u03c0\u03b5\u03c1\u03b9\u03b3\u03c1\u03ac\u03bc\u03bc\u03b1\u03c4\u03bf\u03c2 \u03c3\u03c4\u03b7 \u03b4\u03b5\u03be\u03b9\u03ac \u03c0\u03bb\u03b5\u03c5\u03c1\u03ac */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   \n"
"	background-color: rgb(99, 99, 99);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../../.designer/.designer/.designer/backup/icons/bullet-list-svgrepo-com.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_printOrder.setIcon(icon1)
        self.pushButton_printOrder.setIconSize(QSize(33, 33))
        self.pushButton_printOrder.setCheckable(True)
        self.pushButton_printOrder.setAutoDefault(True)
        self.gridLayoutWidget = QWidget(self.order_tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(650, 40, 501, 791))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_2.setHorizontalSpacing(7)
        self.gridLayout_2.setVerticalSpacing(3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.gridLayoutWidget)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Shadow.Plain)

        self.gridLayout_2.addWidget(self.frame_23, 0, 0, 1, 1)

        self.order.addTab(self.order_tab, "")
        self.label_table_feat.raise_()
        self.webEngineView_2.raise_()
        self.label_17.raise_()
        self.tableWidget_ord.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.pushButton_deleteOrder.raise_()
        self.pushButton_printOrder.raise_()
        self.gridLayoutWidget.raise_()
        self.food_menu = QWidget()
        self.food_menu.setObjectName(u"food_menu")
        self.frame_3 = QFrame(self.food_menu)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 10, 1281, 611))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(10, 0, 701, 91))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_6 = QFrame(self.frame_8)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 40, 611, 51))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_price = QLineEdit(self.frame_6)
        self.lineEdit_price.setObjectName(u"lineEdit_price")
        self.lineEdit_price.setGeometry(QRect(552, 10, 51, 31))
        self.lineEdit_price.setStyleSheet(u"selection-background-color: rgb(184, 184, 184);\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(58, 58, 58);\n"
"background-color: rgb(240, 240, 240);\n"
"border-color: rgb(52, 52, 52);")
        self.lineEdit_category = QLineEdit(self.frame_6)
        self.lineEdit_category.setObjectName(u"lineEdit_category")
        self.lineEdit_category.setGeometry(QRect(10, 10, 151, 31))
        self.lineEdit_category.setStyleSheet(u"selection-background-color: rgb(184, 184, 184);\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(58, 58, 58);\n"
"background-color: rgb(240, 240, 240);\n"
"border-color: rgb(52, 52, 52);")
        self.lineEdit_amount = QLineEdit(self.frame_6)
        self.lineEdit_amount.setObjectName(u"lineEdit_amount")
        self.lineEdit_amount.setGeometry(QRect(490, 10, 51, 31))
        self.lineEdit_amount.setStyleSheet(u"selection-background-color: rgb(184, 184, 184);\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(58, 58, 58);\n"
"background-color: rgb(240, 240, 240);\n"
"border-color: rgb(52, 52, 52);")
        self.lineEdit_description = QLineEdit(self.frame_6)
        self.lineEdit_description.setObjectName(u"lineEdit_description")
        self.lineEdit_description.setGeometry(QRect(167, 10, 311, 31))
        self.lineEdit_description.setStyleSheet(u"selection-background-color: rgb(184, 184, 184);\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(58, 58, 58);\n"
"background-color: rgb(240, 240, 240);\n"
"border-color: rgb(52, 52, 52);")
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(0, 10, 651, 36))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.label_6 = QLabel(self.frame_9)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 131, 16))
        self.label_6.setStyleSheet(u"color: rgb(59, 106, 120);\n"
"font: 9pt \"Segoe UI\";")
        self.label_9 = QLabel(self.frame_9)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(169, 10, 121, 16))
        self.label_9.setStyleSheet(u"color: rgb(59, 106, 120);\n"
"font: 9pt \"Segoe UI\";")
        self.label_10 = QLabel(self.frame_9)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(490, 10, 61, 16))
        self.label_10.setStyleSheet(u"color: rgb(59, 106, 120);\n"
"font: 9pt \"Segoe UI\";")
        self.label_11 = QLabel(self.frame_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(550, 10, 61, 16))
        self.label_11.setStyleSheet(u"color: rgb(59, 106, 120);\n"
"font: 9pt \"Segoe UI\";")
        self.pushButton_submit_item = QPushButton(self.frame_8)
        self.pushButton_submit_item.setObjectName(u"pushButton_submit_item")
        self.pushButton_submit_item.setGeometry(QRect(620, 50, 75, 31))
        self.pushButton_submit_item.setStyleSheet(u"QPushButton {\n"
"    color: rgb(249, 249, 249);\n"
"    border-radius: 0px;\n"
"	\n"
"	\n"
"	font: 8pt \"Segoe UI\";\n"
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
        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(20, 110, 1251, 481))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.label_12 = QLabel(self.frame_10)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 10, 131, 16))
        self.label_12.setStyleSheet(u"color: rgb(59, 106, 120);")
        self.listView_description = QListView(self.frame_10)
        self.listView_description.setObjectName(u"listView_description")
        self.listView_description.setGeometry(QRect(350, 20, 341, 401))
        self.listView_description.setStyleSheet(u"color: rgb(50, 100, 111);")
        self.listView_category = QListView(self.frame_10)
        self.listView_category.setObjectName(u"listView_category")
        self.listView_category.setGeometry(QRect(710, 20, 341, 401))
        self.listView_category.setStyleSheet(u"color: rgb(50, 100, 111);")
        self.productListView = QListView(self.frame_10)
        self.productListView.setObjectName(u"productListView")
        self.productListView.setGeometry(QRect(0, 20, 331, 401))
        self.productListView.setStyleSheet(u"color: rgb(50, 100, 111);")
        self.label_13 = QLabel(self.frame_10)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(730, 10, 131, 16))
        self.label_13.setStyleSheet(u"color: rgb(59, 106, 120);")
        self.label_14 = QLabel(self.frame_10)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(380, 10, 171, 16))
        self.label_14.setStyleSheet(u"color: rgb(59, 106, 120);")
        self.listView_description.raise_()
        self.listView_category.raise_()
        self.productListView.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_12.raise_()
        self.pushButton_delete_item = QPushButton(self.frame_3)
        self.pushButton_delete_item.setObjectName(u"pushButton_delete_item")
        self.pushButton_delete_item.setGeometry(QRect(730, 50, 75, 31))
        self.pushButton_delete_item.setStyleSheet(u"QPushButton {\n"
"    color: rgb(249, 249, 249);\n"
"    border-radius: 0px;\n"
"	\n"
"	\n"
"	font: 8pt \"Segoe UI\";\n"
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
        self.widget = QWidget(self.food_menu)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-10, 620, 751, 141))
        self.frame_7 = QFrame(self.widget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(550, 430, 1291, 191))
        self.frame_7.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.occupation_graph = QGraphicsView(self.frame_7)
        self.occupation_graph.setObjectName(u"occupation_graph")
        self.occupation_graph.setGeometry(QRect(20, 10, 421, 171))
        self.occupation_graph.setFrameShape(QFrame.Shape.NoFrame)
        self.order.addTab(self.food_menu, "")
        self.tab_settings = QWidget()
        self.tab_settings.setObjectName(u"tab_settings")
        self.frame_2 = QFrame(self.tab_settings)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(1310, 60, 341, 141))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.Shape.WinPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.init_tables_2 = QGroupBox(self.frame_2)
        self.init_tables_2.setObjectName(u"init_tables_2")
        self.init_tables_2.setGeometry(QRect(170, 9, 150, 111))
        self.init_tables_2.setStyleSheet(u"")
        self.init_tables_2.setFlat(True)
        self.gridLayout = QGridLayout(self.init_tables_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.save_annonations_2 = QPushButton(self.init_tables_2)
        self.save_annonations_2.setObjectName(u"save_annonations_2")
        self.save_annonations_2.setEnabled(False)
        palette = QPalette()
        brush = QBrush(QColor(235, 122, 9, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(208, 212, 217, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 119, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush2)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush)
        brush3 = QBrush(QColor(235, 122, 9, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.save_annonations_2.setPalette(palette)
        self.save_annonations_2.setFont(font)
        self.save_annonations_2.setStyleSheet(u"")
        self.save_annonations_2.setIconSize(QSize(20, 20))
        self.save_annonations_2.setFlat(True)

        self.gridLayout.addWidget(self.save_annonations_2, 1, 0, 1, 1)

        self.iou_spin_box = QDoubleSpinBox(self.init_tables_2)
        self.iou_spin_box.setObjectName(u"iou_spin_box")
        self.iou_spin_box.setDecimals(2)
        self.iou_spin_box.setMaximum(1.000000000000000)
        self.iou_spin_box.setSingleStep(0.010000000000000)
        self.iou_spin_box.setValue(0.070000000000000)

        self.gridLayout.addWidget(self.iou_spin_box, 0, 1, 1, 1)

        self.conf_spin_box = QDoubleSpinBox(self.init_tables_2)
        self.conf_spin_box.setObjectName(u"conf_spin_box")
        self.conf_spin_box.setMaximum(1.000000000000000)
        self.conf_spin_box.setSingleStep(0.010000000000000)
        self.conf_spin_box.setValue(0.070000000000000)

        self.gridLayout.addWidget(self.conf_spin_box, 1, 1, 1, 1)

        self.annonate_image_2 = QPushButton(self.init_tables_2)
        self.annonate_image_2.setObjectName(u"annonate_image_2")
        self.annonate_image_2.setEnabled(False)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Highlight, brush2)
        palette1.setBrush(QPalette.Active, QPalette.HighlightedText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Highlight, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Highlight, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.annonate_image_2.setPalette(palette1)
        self.annonate_image_2.setFont(font)
        self.annonate_image_2.setStyleSheet(u"selection-color: rgb(235, 122, 9);\n"
"color: rgb(235, 122, 9);")
        self.annonate_image_2.setIconSize(QSize(20, 20))
        self.annonate_image_2.setFlat(True)

        self.gridLayout.addWidget(self.annonate_image_2, 0, 0, 1, 1)

        self.Source = QGroupBox(self.frame_2)
        self.Source.setObjectName(u"Source")
        self.Source.setGeometry(QRect(10, 10, 122, 94))
        self.Source.setMouseTracking(True)
        self.Source.setAcceptDrops(False)
        self.Source.setToolTipDuration(0)
#if QT_CONFIG(whatsthis)
        self.Source.setWhatsThis(u"")
#endif // QT_CONFIG(whatsthis)
        self.Source.setAutoFillBackground(False)
        self.Source.setStyleSheet(u"")
        self.Source.setFlat(True)
        self.Source.setCheckable(False)
        self.toolButton_choose_image = QToolButton(self.Source)
        self.toolButton_choose_image.setObjectName(u"toolButton_choose_image")
        self.toolButton_choose_image.setGeometry(QRect(10, 30, 101, 31))
        self.toolButton_choose_image.setStyleSheet(u"")
        self.toolButton_choose_cam = QToolButton(self.frame_2)
        self.toolButton_choose_cam.setObjectName(u"toolButton_choose_cam")
        self.toolButton_choose_cam.setGeometry(QRect(20, 84, 101, 31))
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dlg 2"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.toolButton_choose_cam.setFont(font2)
        self.toolButton_choose_cam.setStyleSheet(u"")
        self.graphicsView = QGraphicsView(self.tab_settings)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(40, 30, 1251, 731))
        self.graphicsView.setFrameShape(QFrame.Shape.NoFrame)
        self.graphicsView.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_4 = QFrame(self.tab_settings)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(1310, 220, 341, 151))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.annonate_image = QPushButton(self.frame_4)
        self.annonate_image.setObjectName(u"annonate_image")
        self.annonate_image.setEnabled(True)
        self.annonate_image.setGeometry(QRect(20, 20, 125, 51))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush4 = QBrush(QColor(63, 113, 140, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush4)
        brush5 = QBrush(QColor(70, 32, 0, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Highlight, brush5)
        palette2.setBrush(QPalette.Active, QPalette.HighlightedText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Highlight, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Highlight, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.annonate_image.setPalette(palette2)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(8)
        font3.setBold(False)
        font3.setItalic(False)
        self.annonate_image.setFont(font3)
        self.annonate_image.setStyleSheet(u"QPushButton {\n"
"    color: rgb(249, 249, 249);\n"
"    border-radius: 0px;\n"
"	\n"
"	\n"
"	font: 8pt \"Segoe UI\";\n"
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
        self.annonate_image.setIconSize(QSize(20, 20))
        self.annonate_image.setFlat(False)
        self.auto_set_tables = QPushButton(self.frame_4)
        self.auto_set_tables.setObjectName(u"auto_set_tables")
        self.auto_set_tables.setEnabled(False)
        self.auto_set_tables.setGeometry(QRect(200, 20, 125, 51))
        self.auto_set_tables.setMouseTracking(True)
        self.auto_set_tables.setStyleSheet(u"QPushButton {\n"
"    color: rgb(249, 249, 249);\n"
"    border-radius: 0px;\n"
"	\n"
"	\n"
"	font: 8pt \"Segoe UI\";\n"
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
        icon2 = QIcon()
        icon2.addFile(u"../../.designer/.designer/.designer/.designer/backup/circle-play-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.auto_set_tables.setIcon(icon2)
        self.auto_set_tables.setCheckable(False)
        self.auto_set_tables.setAutoDefault(False)
        self.auto_set_tables.setFlat(False)
        self.frame_11 = QFrame(self.tab_settings)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(100, 921, 91, 41))
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.order.addTab(self.tab_settings, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.frame_13 = QFrame(self.tab)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(190, 30, 681, 701))
        self.frame_13.setFrameShape(QFrame.Shape.Box)
        self.frame_13.setFrameShadow(QFrame.Shadow.Sunken)
        self.webEngineView = QWebEngineView(self.frame_13)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setGeometry(QRect(20, 30, 641, 631))
        self.webEngineView.setProperty("url", QUrl(u"about:blank"))
        self.order.addTab(self.tab, "")
        self.frame_30 = QFrame(self.frame)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setGeometry(QRect(20, 60, 181, 761))
        self.frame_30.setStyleSheet(u"color: rgb(255, 195, 99);\n"
"\n"
"font: 500 11pt \"Quicksand Medium\";")
        self.frame_30.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)
        self.widget1 = QWidget(self.frame_30)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(-10, 140, 181, 601))
        self.widget1.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(2, 86, 213);\n"
"    color: rgb(249, 249, 249);\n"
"    border-radius:10px;\n"
"	height: 65px;\n"
"\n"
"    border-right: 15px solid blue /* \u03a0\u03c1\u03bf\u03c3\u03b8\u03ae\u03ba\u03b7 \u03ba\u03af\u03c4\u03c1\u03b9\u03bd\u03b7\u03c2 \u03b3\u03c1\u03b1\u03bc\u03bc\u03ae\u03c2 \u03c0\u03b5\u03c1\u03b9\u03b3\u03c1\u03ac\u03bc\u03bc\u03b1\u03c4\u03bf\u03c2 \u03c3\u03c4\u03b7 \u03b4\u03b5\u03be\u03b9\u03ac \u03c0\u03bb\u03b5\u03c5\u03c1\u03ac */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   \n"
"	background-color: rgb(99, 99, 99);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.run_model_button = QPushButton(self.widget1)
        self.run_model_button.setObjectName(u"run_model_button")
        self.run_model_button.setToolTipDuration(15)
        self.run_model_button.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"../../.designer/.designer/.designer/backup/icons/run.png", QSize(), QIcon.Normal, QIcon.Off)
        self.run_model_button.setIcon(icon3)
        self.run_model_button.setIconSize(QSize(33, 47))
        self.run_model_button.setChecked(False)

        self.verticalLayout.addWidget(self.run_model_button)

        self.frame_27 = QFrame(self.widget1)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setStyleSheet(u"font: 500 11pt \"Quicksand Medium\";")
        self.timer_label = QLabel(self.frame_27)
        self.timer_label.setObjectName(u"timer_label")
        self.timer_label.setGeometry(QRect(0, 30, 61, 21))
        font4 = QFont()
        font4.setFamilies([u"Quicksand Medium"])
        font4.setPointSize(9)
        font4.setWeight(QFont.Medium)
        font4.setItalic(False)
        self.timer_label.setFont(font4)
        self.timer_label.setAutoFillBackground(False)
        self.timer_label.setStyleSheet(u"color: rgb(54, 109, 121);\n"
"font: 500 9pt \"Quicksand Medium\";\n"
"")
        self.timer_label.setScaledContents(True)
        self.timer_label.setWordWrap(False)
        self.timer_spinBox = QSpinBox(self.frame_27)
        self.timer_spinBox.setObjectName(u"timer_spinBox")
        self.timer_spinBox.setGeometry(QRect(70, 30, 51, 24))
        self.timer_spinBox.setStyleSheet(u"color: rgb(5, 135, 175);\n"
"font: 500 11pt \"Roboto Medium\";")
        self.timer_spinBox.setMinimum(0)
        self.timer_spinBox.setMaximum(300)
        self.timer_spinBox.setSingleStep(10)
        self.timer_spinBox.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.timer_spinBox.setValue(30)
        self.timer_label_2 = QLabel(self.frame_27)
        self.timer_label_2.setObjectName(u"timer_label_2")
        self.timer_label_2.setGeometry(QRect(130, 30, 31, 21))
        font5 = QFont()
        font5.setFamilies([u"Quicksand Medium"])
        font5.setPointSize(11)
        font5.setWeight(QFont.Medium)
        font5.setItalic(False)
        self.timer_label_2.setFont(font5)
        self.timer_label_2.setAutoFillBackground(False)
        self.timer_label_2.setStyleSheet(u"color: rgb(54, 109, 121);\n"
"font: 500 11pt \"Quicksand Medium\";")
        self.timer_label_2.setScaledContents(True)
        self.timer_label_2.setWordWrap(False)

        self.verticalLayout.addWidget(self.frame_27)

        self.pushButton_camera_live = QPushButton(self.widget1)
        self.pushButton_camera_live.setObjectName(u"pushButton_camera_live")
        self.pushButton_camera_live.setEnabled(True)
        self.pushButton_camera_live.setMouseTracking(True)
        self.pushButton_camera_live.setTabletTracking(True)
        self.pushButton_camera_live.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"../../.designer/.designer/.designer/backup/icons/icons8-video-camera-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_camera_live.setIcon(icon4)
        self.pushButton_camera_live.setIconSize(QSize(46, 40))
        self.pushButton_camera_live.setAutoDefault(True)

        self.verticalLayout.addWidget(self.pushButton_camera_live)

        self.pushButton_waiters = QPushButton(self.widget1)
        self.pushButton_waiters.setObjectName(u"pushButton_waiters")
        self.pushButton_waiters.setEnabled(True)
        self.pushButton_waiters.setMouseTracking(True)
        self.pushButton_waiters.setTabletTracking(True)
        self.pushButton_waiters.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u"../../.designer/.designer/.designer/backup/icons/dinner-svgrepo-com.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_waiters.setIcon(icon5)
        self.pushButton_waiters.setIconSize(QSize(33, 33))
        self.pushButton_waiters.setAutoDefault(True)
        self.pushButton_waiters.setFlat(False)

        self.verticalLayout.addWidget(self.pushButton_waiters)

        self.pushButton_to_reservations = QPushButton(self.widget1)
        self.pushButton_to_reservations.setObjectName(u"pushButton_to_reservations")
        self.pushButton_to_reservations.setEnabled(True)
        self.pushButton_to_reservations.setMouseTracking(True)
        self.pushButton_to_reservations.setTabletTracking(True)
        self.pushButton_to_reservations.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u"../../.designer/.designer/.designer/backup/icons/clock-svgrepo-com.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_to_reservations.setIcon(icon6)
        self.pushButton_to_reservations.setIconSize(QSize(33, 33))
        self.pushButton_to_reservations.setAutoDefault(True)

        self.verticalLayout.addWidget(self.pushButton_to_reservations)

        self.pushButton_to_statistics = QPushButton(self.widget1)
        self.pushButton_to_statistics.setObjectName(u"pushButton_to_statistics")
        self.pushButton_to_statistics.setEnabled(True)
        self.pushButton_to_statistics.setMouseTracking(True)
        self.pushButton_to_statistics.setTabletTracking(True)
        self.pushButton_to_statistics.setStyleSheet(u"")
        self.pushButton_to_statistics.setIcon(icon6)
        self.pushButton_to_statistics.setIconSize(QSize(33, 33))
        self.pushButton_to_statistics.setAutoDefault(True)

        self.verticalLayout.addWidget(self.pushButton_to_statistics)

        self.line_4 = QFrame(self.frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(200, -10, 20, 931))
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.frame_14 = QFrame(self.frame)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(0, 940, 1921, 61))
        self.frame_14.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(255, 255, 255);")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.label_19 = QLabel(self.frame_14)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(0, 0, 211, 61))
        self.label_19.setStyleSheet(u"font: 9pt \"Segoe UI\";\n"
"background-color: rgb(43, 104, 130);\n"
"")
        self.line_9 = QFrame(self.frame_14)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(510, 10, 16, 41))
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)
        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(530, 10, 435, 41))
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_20 = QLabel(self.frame_16)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"color: rgb(40, 105, 120);\n"
"font: 11pt \"Tahoma\";")

        self.horizontalLayout_4.addWidget(self.label_20)

        self.label_number_of_tables = QLabel(self.frame_16)
        self.label_number_of_tables.setObjectName(u"label_number_of_tables")
        self.label_number_of_tables.setStyleSheet(u"color: rgb(70, 70, 70);\n"
"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_4.addWidget(self.label_number_of_tables)

        self.line_3 = QFrame(self.frame_16)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_3)

        self.label_23 = QLabel(self.frame_16)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"color: rgb(40, 105, 120);\n"
"font: 11pt \"Tahoma\";")

        self.horizontalLayout_4.addWidget(self.label_23)

        self.label_occupied_tables = QLabel(self.frame_16)
        self.label_occupied_tables.setObjectName(u"label_occupied_tables")
        self.label_occupied_tables.setStyleSheet(u"color: rgb(255, 19, 19);\n"
"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_4.addWidget(self.label_occupied_tables)

        self.line_10 = QFrame(self.frame_16)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_10)

        self.label_24 = QLabel(self.frame_16)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"color: rgb(40, 105, 120);\n"
"font: 11pt \"Tahoma\";")

        self.horizontalLayout_4.addWidget(self.label_24)

        self.label_free_tables = QLabel(self.frame_16)
        self.label_free_tables.setObjectName(u"label_free_tables")
        self.label_free_tables.setStyleSheet(u"color: rgb(44, 159, 140);\n"
"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_4.addWidget(self.label_free_tables)

        self.label_25 = QLabel(self.frame_14)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(240, 10, 241, 41))
        self.label_25.setStyleSheet(u"color: rgb(89, 89, 89);\n"
"font: 11pt \"Segoe UI\";")
        self.frame_12 = QFrame(self.frame_14)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(360, 10, 151, 41))
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.green_led = QGraphicsView(self.frame_14)
        self.green_led.setObjectName(u"green_led")
        self.green_led.setGeometry(QRect(450, 20, 28, 21))
        self.green_led.setMinimumSize(QSize(15, 20))
        self.green_led.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"")
        self.green_led.setFrameShape(QFrame.Shape.NoFrame)
        self.red_led = QGraphicsView(self.frame_14)
        self.red_led.setObjectName(u"red_led")
        self.red_led.setGeometry(QRect(360, 20, 31, 21))
        self.red_led.setMinimumSize(QSize(15, 20))
        self.red_led.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"")
        self.red_led.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_30.raise_()
        self.order.raise_()
        self.line_4.raise_()
        self.frame_14.raise_()

        self.horizontalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.order.setCurrentIndex(0)
        self.annonate_image.setDefault(True)
        self.auto_set_tables.setDefault(False)
        self.pushButton_camera_live.setDefault(True)
        self.pushButton_waiters.setDefault(True)
        self.pushButton_to_reservations.setDefault(True)
        self.pushButton_to_statistics.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Tables Occupation Time", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Notify in", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.reset_occupation_time.setText(QCoreApplication.translate("MainWindow", u"     Reset Occupation", None))
        self.order.setTabText(self.order.indexOf(self.tab_overview), QCoreApplication.translate("MainWindow", u"Overview", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Ready Orders", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Preparing Orders", None))
        self.label_table_feat.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Tables Service Overview", None))
        self.pushButton_deleteOrder.setText(QCoreApplication.translate("MainWindow", u"Delete Order", None))
        self.pushButton_printOrder.setText(QCoreApplication.translate("MainWindow", u"Print Order", None))
        self.order.setTabText(self.order.indexOf(self.order_tab), QCoreApplication.translate("MainWindow", u"Orders", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.pushButton_submit_item.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Recent Records", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Search by Category", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Search by Description", None))
        self.pushButton_delete_item.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.order.setTabText(self.order.indexOf(self.food_menu), QCoreApplication.translate("MainWindow", u"Food Menu", None))
        self.init_tables_2.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.save_annonations_2.setText(QCoreApplication.translate("MainWindow", u"Conf", None))
        self.annonate_image_2.setText(QCoreApplication.translate("MainWindow", u"Iou", None))
        self.Source.setTitle(QCoreApplication.translate("MainWindow", u"Source", None))
        self.toolButton_choose_image.setText(QCoreApplication.translate("MainWindow", u"Choose Image", None))
        self.toolButton_choose_cam.setText(QCoreApplication.translate("MainWindow", u"Choose Source", None))
        self.annonate_image.setText(QCoreApplication.translate("MainWindow", u"Manual Set Tables", None))
        self.auto_set_tables.setText(QCoreApplication.translate("MainWindow", u"Auto Tables", None))
        self.order.setTabText(self.order.indexOf(self.tab_settings), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.order.setTabText(self.order.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"New Order", None))
#if QT_CONFIG(tooltip)
        self.run_model_button.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.run_model_button.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.run_model_button.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.run_model_button.setText(QCoreApplication.translate("MainWindow", u"Run Detection", None))
        self.timer_label.setText(QCoreApplication.translate("MainWindow", u"Run every", None))
        self.timer_spinBox.setSuffix("")
        self.timer_label_2.setText(QCoreApplication.translate("MainWindow", u"sec", None))
#if QT_CONFIG(accessibility)
        self.pushButton_camera_live.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.pushButton_camera_live.setText(QCoreApplication.translate("MainWindow", u"Live Camera", None))
#if QT_CONFIG(accessibility)
        self.pushButton_waiters.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.pushButton_waiters.setText(QCoreApplication.translate("MainWindow", u"Waiters", None))
#if QT_CONFIG(accessibility)
        self.pushButton_to_reservations.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.pushButton_to_reservations.setText(QCoreApplication.translate("MainWindow", u"Reservation", None))
#if QT_CONFIG(accessibility)
        self.pushButton_to_statistics.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.pushButton_to_statistics.setText(QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"                      DignSight 1.0.2 ", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Tables :", None))
        self.label_number_of_tables.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Occupied : ", None))
        self.label_occupied_tables.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Free : ", None))
        self.label_free_tables.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Detection Server", None))
    # retranslateUi

