# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Examer(object):
    def setupUi(self, Examer):
        if not Examer.objectName():
            Examer.setObjectName(u"Examer")
        Examer.resize(431, 150)
        Examer.setStyleSheet(u"background-color: rgb(0, 29, 31)")
        self.widget = QWidget(Examer)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 431, 147))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(Examer)

        QMetaObject.connectSlotsByName(Examer)
    # setupUi

    def retranslateUi(self, Examer):
        Examer.setWindowTitle(QCoreApplication.translate("Examer", u"Examer", None))
        self.label.setText(QCoreApplication.translate("Examer", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0444\u0430\u043c\u0438\u043b\u0438\u044e:", None))
        self.label_2.setText(QCoreApplication.translate("Examer", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0435\u0441\u0442:", None))
        self.pushButton.setText(QCoreApplication.translate("Examer", u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438 \u043a \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044e", None))
    # retranslateUi

