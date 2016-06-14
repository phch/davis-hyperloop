# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Tue Jun 14 13:31:39 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pingButton = QtGui.QPushButton(self.centralwidget)
        self.pingButton.setObjectName(_fromUtf8("pingButton"))
        self.verticalLayout.addWidget(self.pingButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.ipLabel = QtGui.QLabel(self.centralwidget)
        self.ipLabel.setObjectName(_fromUtf8("ipLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.ipLabel)
        self.ipLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.ipLineEdit.setObjectName(_fromUtf8("ipLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.ipLineEdit)
        self.portLabel = QtGui.QLabel(self.centralwidget)
        self.portLabel.setObjectName(_fromUtf8("portLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.portLabel)
        self.portLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.portLineEdit.setObjectName(_fromUtf8("portLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.portLineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pingButton.setText(_translate("MainWindow", "Ping", None))
        self.ipLabel.setText(_translate("MainWindow", "IP", None))
        self.portLabel.setText(_translate("MainWindow", "Port", None))

