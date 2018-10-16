# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_ImgViewer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ImgViewer(object):
    def setupUi(self, ImgViewer):
        ImgViewer.setObjectName("ImgViewer")
        ImgViewer.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ImgViewer)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.imgView = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgView.sizePolicy().hasHeightForWidth())
        self.imgView.setSizePolicy(sizePolicy)
        self.imgView.setText("")
        self.imgView.setObjectName("imgView")
        self.horizontalLayout.addWidget(self.imgView)
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setObjectName("treeView")
        self.horizontalLayout.addWidget(self.treeView)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        ImgViewer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ImgViewer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        ImgViewer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ImgViewer)
        self.statusbar.setObjectName("statusbar")
        ImgViewer.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(ImgViewer)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(ImgViewer)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(ImgViewer)
        self.actionClose.triggered.connect(ImgViewer.close)
        QtCore.QMetaObject.connectSlotsByName(ImgViewer)

    def retranslateUi(self, ImgViewer):
        _translate = QtCore.QCoreApplication.translate
        ImgViewer.setWindowTitle(_translate("ImgViewer", "MainWindow"))
        self.menuFile.setTitle(_translate("ImgViewer", "File"))
        self.actionOpen.setText(_translate("ImgViewer", "Open"))
        self.actionClose.setText(_translate("ImgViewer", "Close"))

