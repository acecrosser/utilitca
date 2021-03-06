# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interFace.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from functions import data_path


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(393, 625)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QSize(393, 625))
        mainWindow.setMaximumSize(QSize(393, 625))
        font = QFont()
        font.setFamily(u"Arial")
        mainWindow.setFont(font)
        icon = QIcon()
        iconThemeName = u"ico"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(f"{data_path}util_ico.png", QSize(), QIcon.Normal, QIcon.Off)
            icon.addFile(f"{data_path}util_ico.png", QSize(), QIcon.Normal, QIcon.On)
        
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(11, 293, 370, 24))
        self.comboBox.setLayoutDirection(Qt.LeftToRight)
        self.comboBox.setEditable(False)
        self.comboBox.setModelColumn(0)
        self.serial_fn = QLineEdit(self.centralwidget)
        self.serial_fn.setObjectName(u"serial_fn")
        self.serial_fn.setGeometry(QRect(11, 463, 370, 24))
        self.serial_kkt = QLineEdit(self.centralwidget)
        self.serial_kkt.setObjectName(u"serial_kkt")
        self.serial_kkt.setGeometry(QRect(11, 409, 370, 24))
        self.label_kkt_serial = QLabel(self.centralwidget)
        self.label_kkt_serial.setObjectName(u"label_kkt_serial")
        self.label_kkt_serial.setGeometry(QRect(11, 386, 132, 16))
        self.label_kkt = QLabel(self.centralwidget)
        self.label_kkt.setObjectName(u"label_kkt")
        self.label_kkt.setGeometry(QRect(11, 332, 74, 16))
        self.model_kkt = QLineEdit(self.centralwidget)
        self.model_kkt.setObjectName(u"model_kkt")
        self.model_kkt.setGeometry(QRect(11, 355, 370, 24))
        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(11, 494, 100, 16))
        self.spec_name = QLineEdit(self.centralwidget)
        self.spec_name.setObjectName(u"spec_name")
        self.spec_name.setGeometry(QRect(11, 517, 370, 24))
        self.label_fn = QLabel(self.centralwidget)
        self.label_fn.setObjectName(u"label_fn")
        self.label_fn.setGeometry(QRect(11, 440, 129, 16))
        self.label_kpp = QLabel(self.centralwidget)
        self.label_kpp.setObjectName(u"label_kpp")
        self.label_kpp.setGeometry(QRect(11, 119, 26, 16))
        self.name_company = QLineEdit(self.centralwidget)
        self.name_company.setObjectName(u"name_company")
        self.name_company.setGeometry(QRect(11, 34, 370, 24))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(37)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.name_company.sizePolicy().hasHeightForWidth())
        self.name_company.setSizePolicy(sizePolicy1)
        self.name_company.setMinimumSize(QSize(370, 0))
        self.kpp_company = QLineEdit(self.centralwidget)
        self.kpp_company.setObjectName(u"kpp_company")
        self.kpp_company.setGeometry(QRect(11, 142, 370, 24))
        sizePolicy.setHeightForWidth(self.kpp_company.sizePolicy().hasHeightForWidth())
        self.kpp_company.setSizePolicy(sizePolicy)
        self.label_address = QLabel(self.centralwidget)
        self.label_address.setObjectName(u"label_address")
        self.label_address.setGeometry(QRect(11, 227, 38, 16))
        self.address_work = QLineEdit(self.centralwidget)
        self.address_work.setObjectName(u"address_work")
        self.address_work.setGeometry(QRect(11, 250, 370, 24))
        sizePolicy.setHeightForWidth(self.address_work.sizePolicy().hasHeightForWidth())
        self.address_work.setSizePolicy(sizePolicy)
        self.label_inn = QLabel(self.centralwidget)
        self.label_inn.setObjectName(u"label_inn")
        self.label_inn.setGeometry(QRect(11, 65, 27, 16))
        self.number_bill = QLineEdit(self.centralwidget)
        self.number_bill.setObjectName(u"number_bill")
        self.number_bill.setGeometry(QRect(11, 196, 370, 24))
        sizePolicy.setHeightForWidth(self.number_bill.sizePolicy().hasHeightForWidth())
        self.number_bill.setSizePolicy(sizePolicy)
        self.label_bill = QLabel(self.centralwidget)
        self.label_bill.setObjectName(u"label_bill")
        self.label_bill.setGeometry(QRect(11, 173, 51, 16))
        self.inn_company = QLineEdit(self.centralwidget)
        self.inn_company.setObjectName(u"inn_company")
        self.inn_company.setGeometry(QRect(11, 88, 370, 24))
        sizePolicy.setHeightForWidth(self.inn_company.sizePolicy().hasHeightForWidth())
        self.inn_company.setSizePolicy(sizePolicy)
        self.label_company = QLabel(self.centralwidget)
        self.label_company.setObjectName(u"label_company")
        self.label_company.setGeometry(QRect(11, 11, 92, 16))
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(11, 560, 370, 35))
        self.splitter.setOrientation(Qt.Horizontal)
        self.printReestr = QPushButton(self.splitter)
        self.printReestr.setObjectName(u"printReestr")
        self.splitter.addWidget(self.printReestr)
        self.makeEmail = QPushButton(self.splitter)
        self.makeEmail.setObjectName(u"makeEmail")
        self.splitter.addWidget(self.makeEmail)
        self.printRequest = QPushButton(self.splitter)
        self.printRequest.setObjectName(u"printRequest")
        self.splitter.addWidget(self.printRequest)
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(60, 600, 271, 17))
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        self.comboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\u0423\u0442\u0438\u043b\u0438\u0442\u0430 \u0432\u043d\u0435\u0434\u0440\u0435\u043d\u0438\u044f", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("mainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f \u0438 \u0444\u0438\u0441\u043a\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u043e\u0434\u043d\u043e\u0439 \u0435\u0434\u0438\u043d\u0438\u0446\u044b \u041a\u041a\u0422", u"first_"))
        self.comboBox.setItemText(1, QCoreApplication.translate("mainWindow", u"\u041a\u043e\u043c\u043f\u043b\u0435\u043a\u0441\u043d\u0430\u044f \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u041a\u043e\u043d\u0442\u0443\u0440.\u041c\u0430\u0440\u043a\u0435\u0442\u0430", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("mainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u041a\u043e\u043d\u0442\u0443\u0440.\u041c\u0430\u0440\u043a\u0435\u0442\u0430", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("mainWindow", u"\u041f\u0435\u0440\u0435\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f \u041a\u041a\u0422 \u0431\u0435\u0437 \u0437\u0430\u043c\u0435\u043d\u044b  \u0424\u041d", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("mainWindow", u"\u041f\u0435\u0440\u0435\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f \u041a\u041a\u0422 \u0441 \u0437\u0430\u043c\u0435\u043d\u043e\u0439  \u0424\u041d", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("mainWindow", u"\u0421\u043d\u044f\u0442\u0438\u0435 \u0441 \u0443\u0447\u0435\u0442\u0430 \u041a\u041a\u0422", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("mainWindow", u"\u041f\u0440\u043e\u0448\u0438\u0432\u043a\u0430 \u041a\u041a\u0422", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("mainWindow", u"\u041f\u0443\u0441\u0442\u043e\u0439 \u0431\u043b\u0430\u043d\u043a", None))

        self.label_kkt_serial.setText(QCoreApplication.translate("mainWindow", u"\u0417\u0430\u0432\u043e\u0434\u0441\u043a\u043e\u0439 \u043d\u043e\u043c\u0435\u0440 \u041a\u041a\u0422", None))
        self.label_kkt.setText(QCoreApplication.translate("mainWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c \u041a\u041a\u0422", None))
        self.label_name.setText(QCoreApplication.translate("mainWindow", u"\u0424\u0418\u041e \u0412\u043d\u0435\u0434\u0440\u0435\u043d\u0446\u0430", None))
        self.spec_name.setText("")
        self.label_fn.setText(QCoreApplication.translate("mainWindow", u"\u0417\u0430\u0432\u043e\u0434c\u043a\u043e\u0439 \u043d\u043e\u043c\u0435\u0440 \u0424\u041d", None))
        self.label_kpp.setText(QCoreApplication.translate("mainWindow", u"\u041a\u041f\u041f", None))
        self.label_address.setText(QCoreApplication.translate("mainWindow", u"\u0410\u0434\u0440\u0435\u0441", None))
        self.label_inn.setText(QCoreApplication.translate("mainWindow", u"\u0418\u041d\u041d", None))
        self.label_bill.setText(QCoreApplication.translate("mainWindow", u"\u2116 \u0441\u0447\u0435\u0442\u0430", None))
        self.label_company.setText(QCoreApplication.translate("mainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 ", None))
        self.printReestr.setText(QCoreApplication.translate("mainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0440\u0435\u0435\u0441\u0442\u0440", None))
        self.makeEmail.setText(QCoreApplication.translate("mainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043f\u0438\u0441\u044c\u043c\u043e", None))
        self.printRequest.setText(QCoreApplication.translate("mainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0437\u0430\u044f\u0432\u043a\u0443", None))
        self.checkBox.setText(QCoreApplication.translate("mainWindow", u"\u041f\u0440\u0438\u043a\u0440\u0435\u043f\u0438\u0442\u044c \u043a \u043f\u0438\u0441\u044c\u043c\u0443 \u0437\u0430\u044f\u0432\u043a\u0443 \u043d\u0430 \u043e\u043a\u0430\u0437\u0430\u043d\u0438\u0435 \u0440\u0430\u0431\u043e\u0442", None))
    # retranslateUi

