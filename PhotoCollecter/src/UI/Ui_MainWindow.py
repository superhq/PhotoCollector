# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.srcEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.srcEdit.setEnabled(False)
        self.srcEdit.setObjectName("srcEdit")
        self.gridLayout_2.addWidget(self.srcEdit, 0, 1, 1, 1)
        self.destPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.destPushButton.setObjectName("destPushButton")
        self.gridLayout_2.addWidget(self.destPushButton, 1, 2, 1, 1)
        self.srcPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.srcPushButton.setObjectName("srcPushButton")
        self.gridLayout_2.addWidget(self.srcPushButton, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.collectPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.collectPushButton.setObjectName("collectPushButton")
        self.gridLayout_2.addWidget(self.collectPushButton, 3, 2, 1, 1)
        self.destEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.destEdit.setEnabled(False)
        self.destEdit.setObjectName("destEdit")
        self.gridLayout_2.addWidget(self.destEdit, 1, 1, 1, 1)
        self.chart = QChartView(self.centralwidget)
        self.chart.setObjectName("chart")
        self.gridLayout_2.addWidget(self.chart, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.destPushButton.setText(_translate("MainWindow", "选择"))
        self.srcPushButton.setText(_translate("MainWindow", "选择"))
        self.label_2.setText(_translate("MainWindow", "整理到："))
        self.label.setText(_translate("MainWindow", "待处理："))
        self.collectPushButton.setText(_translate("MainWindow", "收集"))

from PyQt5.QtChart import QChartView
