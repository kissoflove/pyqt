# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogUi.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(311, 507)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 40, 291, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.quesButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.quesButton.setObjectName("quesButton")
        self.gridLayout.addWidget(self.quesButton, 0, 1, 1, 1)
        self.infoButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.infoButton.setObjectName("infoButton")
        self.gridLayout.addWidget(self.infoButton, 0, 0, 1, 1)
        self.criticalButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.criticalButton.setObjectName("criticalButton")
        self.gridLayout.addWidget(self.criticalButton, 1, 1, 1, 1)
        self.warningButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.warningButton.setObjectName("warningButton")
        self.gridLayout.addWidget(self.warningButton, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 190, 71, 16))
        self.label_2.setObjectName("label_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 210, 291, 131))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(30, 0, 30, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(40, 350, 211, 61))
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(10)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 1234567890.0)
        self.lcdNumber.setProperty("intValue", 1234567890)
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 430, 121, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 311, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.infoButton.clicked.connect(MainWindow.infoButton_clicked)
        self.quesButton.clicked.connect(MainWindow.quesButton_clicked)
        self.warningButton.clicked.connect(MainWindow.warningButton_clicked)
        self.criticalButton.clicked.connect(MainWindow.criticalButton_clicked)
        self.pushButton.clicked.connect(MainWindow.getStringButton_clicked)
        self.pushButton_2.clicked.connect(MainWindow.getIntButton_clicked)
        self.pushButton_3.clicked.connect(MainWindow.getComboButton_clicked)
        self.pushButton_4.clicked.connect(MainWindow.showMyDialog)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.quesButton.setText(_translate("MainWindow", "问题框"))
        self.infoButton.setText(_translate("MainWindow", "信息框"))
        self.criticalButton.setText(_translate("MainWindow", "严重警告框"))
        self.warningButton.setText(_translate("MainWindow", "警告框"))
        self.label.setText(_translate("MainWindow", "基本对话框"))
        self.label_2.setText(_translate("MainWindow", "标准对话框"))
        self.pushButton_2.setText(_translate("MainWindow", "获取整型"))
        self.pushButton.setText(_translate("MainWindow", "获取字符串"))
        self.pushButton_3.setText(_translate("MainWindow", "下拉框"))
        self.pushButton_4.setText(_translate("MainWindow", "自定义对话框"))

