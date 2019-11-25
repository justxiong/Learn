# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather.ui'
#
# Created: Fri Nov 22 15:20:35 2019
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
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(110, 100, 401, 211))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.labSelCity = QtWidgets.QLabel(self.formLayoutWidget)
        self.labSelCity.setObjectName("labSelCity")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labSelCity)
        self.cmbPro = QtWidgets.QComboBox(self.formLayoutWidget)
        self.cmbPro.setObjectName("cmbPro")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cmbPro)
        self.labInputCity = QtWidgets.QLabel(self.formLayoutWidget)
        self.labInputCity.setObjectName("labInputCity")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labInputCity)
        self.labShowCity = QtWidgets.QLabel(self.formLayoutWidget)
        self.labShowCity.setObjectName("labShowCity")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labShowCity)
        self.textEditShowcity = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEditShowcity.setObjectName("textEditShowcity")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textEditShowcity)
        self.cmbCity = QtWidgets.QComboBox(self.formLayoutWidget)
        self.cmbCity.setObjectName("cmbCity")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cmbCity)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
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
        self.labSelCity.setText(_translate("MainWindow", "省份"))
        self.labInputCity.setText(_translate("MainWindow", "城市"))
        self.labShowCity.setText(_translate("MainWindow", "天气"))

