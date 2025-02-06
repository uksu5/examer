# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled_2.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)
import res

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 603)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        MainWindow.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 29, 31)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Tabel_Frame = QFrame(self.centralwidget)
        self.Tabel_Frame.setObjectName(u"Tabel_Frame")
        self.Tabel_Frame.setGeometry(QRect(0, 0, 181, 601))
        self.Tabel_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Tabel_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.tableView = QTableView(self.Tabel_Frame)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(0, 20, 181, 581))
        self.TableName_Label = QLabel(self.Tabel_Frame)
        self.TableName_Label.setObjectName(u"TableName_Label")
        self.TableName_Label.setGeometry(QRect(10, 0, 101, 16))
        self.QuestionFrame = QFrame(self.centralwidget)
        self.QuestionFrame.setObjectName(u"QuestionFrame")
        self.QuestionFrame.setGeometry(QRect(190, 70, 601, 241))
        self.QuestionFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.QuestionFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.QuestionText_Label = QLabel(self.QuestionFrame)
        self.QuestionText_Label.setObjectName(u"QuestionText_Label")
        self.QuestionText_Label.setGeometry(QRect(10, 10, 581, 221))
        self.QuestionText_Label.setTextFormat(Qt.TextFormat.RichText)
        self.QuestionText_Label.setScaledContents(False)
        self.QuestionText_Label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.QuestionName_Frame = QFrame(self.centralwidget)
        self.QuestionName_Frame.setObjectName(u"QuestionName_Frame")
        self.QuestionName_Frame.setEnabled(True)
        self.QuestionName_Frame.setGeometry(QRect(190, 20, 601, 36))
        self.QuestionName_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.QuestionName_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.QuestionName_Frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.QuestionName_label = QLabel(self.QuestionName_Frame)
        self.QuestionName_label.setObjectName(u"QuestionName_label")

        self.verticalLayout.addWidget(self.QuestionName_label)

        self.TextInput_Frame = QFrame(self.centralwidget)
        self.TextInput_Frame.setObjectName(u"TextInput_Frame")
        self.TextInput_Frame.setEnabled(True)
        self.TextInput_Frame.setGeometry(QRect(190, 320, 601, 81))
        self.TextInput_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.TextInput_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.TextInput_Frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.TIF_Edit = QLineEdit(self.TextInput_Frame)
        self.TIF_Edit.setObjectName(u"TIF_Edit")
        self.TIF_Edit.setEnabled(False)

        self.gridLayout.addWidget(self.TIF_Edit, 0, 0, 1, 2)

        self.TimerIcon_Label = QLabel(self.centralwidget)
        self.TimerIcon_Label.setObjectName(u"TimerIcon_Label")
        self.TimerIcon_Label.setGeometry(QRect(190, 570, 31, 31))
        self.TimerIcon_Label.setPixmap(QPixmap(u":/icons/icons/clock.png"))
        self.Timer_Label = QLabel(self.centralwidget)
        self.Timer_Label.setObjectName(u"Timer_Label")
        self.Timer_Label.setGeometry(QRect(220, 570, 91, 31))
        self.CheckBox_Frame = QFrame(self.centralwidget)
        self.CheckBox_Frame.setObjectName(u"CheckBox_Frame")
        self.CheckBox_Frame.setGeometry(QRect(190, 320, 601, 151))
        self.CheckBox_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.CheckBox_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.CheckBox_Frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBox_1 = QCheckBox(self.CheckBox_Frame)
        self.checkBox_1.setObjectName(u"checkBox_1")

        self.verticalLayout_2.addWidget(self.checkBox_1)

        self.checkBox_2 = QCheckBox(self.CheckBox_Frame)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_2.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.CheckBox_Frame)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_2.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.CheckBox_Frame)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout_2.addWidget(self.checkBox_4)

        self.RadioBox_Frame = QFrame(self.centralwidget)
        self.RadioBox_Frame.setObjectName(u"RadioBox_Frame")
        self.RadioBox_Frame.setGeometry(QRect(190, 320, 601, 151))
        self.RadioBox_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RadioBox_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.RadioBox_Frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.radioButton_1 = QRadioButton(self.RadioBox_Frame)
        self.radioButton_1.setObjectName(u"radioButton_1")

        self.verticalLayout_3.addWidget(self.radioButton_1)

        self.radioButton_2 = QRadioButton(self.RadioBox_Frame)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_3.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.RadioBox_Frame)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_3.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.RadioBox_Frame)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.verticalLayout_3.addWidget(self.radioButton_4)

        self.EnterAnswer = QPushButton(self.centralwidget)
        self.EnterAnswer.setObjectName(u"EnterAnswer")
        self.EnterAnswer.setGeometry(QRect(190, 510, 601, 51))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.EnterAnswer.setFont(font)
#if QT_CONFIG(accessibility)
        self.EnterAnswer.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.EnterAnswer.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.EnterAnswer.setStyleSheet(u"QPushButton {\n"
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
        self.EnterAnswer.setAutoDefault(False)
        self.EnterAnswer.setFlat(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Examer", None))
        self.TableName_Label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u043e\u043a \u0437\u0430\u0434\u0430\u043d\u0438\u0439:", None))
        self.QuestionText_Label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.QuestionName_label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0432\u043e\u043f\u0440\u043e\u0441\u0430", None))
        self.TIF_Edit.setText("")
        self.TimerIcon_Label.setText("")
        self.Timer_Label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">00:00</span></p></body></html>", None))
        self.checkBox_1.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton_1.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.EnterAnswer.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u043e\u0442\u0432\u0435\u0442", None))
    # retranslateUi

