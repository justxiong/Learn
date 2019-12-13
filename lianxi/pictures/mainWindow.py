# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Wed Dec  4 23:57:22 2019
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelImg = QtWidgets.QLabel(self.centralwidget)
        self.labelImg.setGeometry(QtCore.QRect(90, 30, 411, 341))
        self.labelImg.setObjectName("labelImg")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(150, 390, 279, 70))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnSelect = QtWidgets.QPushButton(self.widget)
        self.btnSelect.setObjectName("btnSelect")
        self.verticalLayout.addWidget(self.btnSelect)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnPriv = QtWidgets.QPushButton(self.widget)
        self.btnPriv.setObjectName("btnPriv")
        self.horizontalLayout.addWidget(self.btnPriv)
        self.btnPP = QtWidgets.QPushButton(self.widget)
        self.btnPP.setObjectName("btnPP")
        self.horizontalLayout.addWidget(self.btnPP)
        self.btnNext = QtWidgets.QPushButton(self.widget)
        self.btnNext.setObjectName("btnNext")
        self.horizontalLayout.addWidget(self.btnNext)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
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
        self.labelImg.setText(_translate("MainWindow", "                                                   PIC View"))
        self.btnSelect.setText(_translate("MainWindow", "选择"))
        self.btnPriv.setText(_translate("MainWindow", "Priv"))
        self.btnPP.setText(_translate("MainWindow", "Play/Pause"))
        self.btnNext.setText(_translate("MainWindow", "Next"))

