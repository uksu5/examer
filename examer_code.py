# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'examer_ap.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTableView,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(824, 612)
        MainWindow.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        MainWindow.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 80, 801, 521))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.tableView = QTableView(self.frame)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 10, 781, 501))
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 801, 61))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.load_test = QPushButton(self.frame_2)
        self.load_test.setObjectName(u"load_test")
        self.load_test.setGeometry(QRect(10, 20, 101, 31))
        self.load_test.setStyleSheet(u"QPushButton {\n"
"    /* \u0421\u0442\u0438\u043b\u044c \u043e\u0431\u044b\u0447\u043d\u043e\u0433\u043e \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #4287f5, stop:1 #1e6ae8);\n"
"    border: 1px solid #1e6ae8;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* \u0421\u0442\u0438\u043b\u044c \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043c\u044b\u0448\u0438 */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #63a3ff, stop:1 #4287f5);\n"
"    border: 1px solid #4287f5;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* \u0421\u0442\u0438\u043b\u044c \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #333333, stop:1 #555555);\n"
"    border: 1px solid #333333;\n"
"}")
        self.settings_button = QPushButton(self.frame_2)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setGeometry(QRect(620, 20, 101, 31))
        self.settings_button.setStyleSheet(u"QPushButton {\n"
"    /* \u0421\u0442\u0438\u043b\u044c \u043e\u0431\u044b\u0447\u043d\u043e\u0433\u043e \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #4287f5, stop:1 #1e6ae8);\n"
"    border: 1px solid #1e6ae8;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* \u0421\u0442\u0438\u043b\u044c \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043c\u044b\u0448\u0438 */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #63a3ff, stop:1 #4287f5);\n"
"    border: 1px solid #4287f5;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* \u0421\u0442\u0438\u043b\u044c \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #333333, stop:1 #555555);\n"
"    border: 1px solid #333333;\n"
"}")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(729, 0, 71, 61))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 61, 61))
        self.label.setPixmap(QPixmap(u":/newPrefix/\u0420\u0435\u0441\u0443\u0440\u0441 2@0.5x.png"))
        self.save_table = QPushButton(self.frame_2)
        self.save_table.setObjectName(u"save_table")
        self.save_table.setGeometry(QRect(120, 20, 121, 31))
        self.save_table.setStyleSheet(u"QPushButton {\n"
"    /* \u0421\u0442\u0438\u043b\u044c \u043e\u0431\u044b\u0447\u043d\u043e\u0433\u043e \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #4287f5, stop:1 #1e6ae8);\n"
"    border: 1px solid #1e6ae8;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* \u0421\u0442\u0438\u043b\u044c \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043c\u044b\u0448\u0438 */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #63a3ff, stop:1 #4287f5);\n"
"    border: 1px solid #4287f5;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* \u0421\u0442\u0438\u043b\u044c \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #333333, stop:1 #555555);\n"
"    border: 1px solid #333333;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Examer Admin Panel", None))
        self.load_test.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0442\u0438\u0442\u044c \u0442\u0435\u0441\u0442 ", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label.setText("")
        self.save_table.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432 *.	XLS", None))
    # retranslateUi

