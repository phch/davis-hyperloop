# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'network_dialog.ui'
#
# Created: Thu Jul  7 14:27:44 2016
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

class Ui_NetworkDialog(object):
    def setupUi(self, NetworkDialog):
        NetworkDialog.setObjectName(_fromUtf8("NetworkDialog"))
        NetworkDialog.resize(400, 101)
        self.verticalLayout = QtGui.QVBoxLayout(NetworkDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.remoteSettingsForm = QtGui.QFormLayout()
        self.remoteSettingsForm.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.remoteSettingsForm.setObjectName(_fromUtf8("remoteSettingsForm"))
        self.remoteHostLabel = QtGui.QLabel(NetworkDialog)
        self.remoteHostLabel.setObjectName(_fromUtf8("remoteHostLabel"))
        self.remoteSettingsForm.setWidget(0, QtGui.QFormLayout.LabelRole, self.remoteHostLabel)
        self.remoteHostLineEdit = QtGui.QLineEdit(NetworkDialog)
        self.remoteHostLineEdit.setObjectName(_fromUtf8("remoteHostLineEdit"))
        self.remoteSettingsForm.setWidget(0, QtGui.QFormLayout.FieldRole, self.remoteHostLineEdit)
        self.remotePortLabel = QtGui.QLabel(NetworkDialog)
        self.remotePortLabel.setObjectName(_fromUtf8("remotePortLabel"))
        self.remoteSettingsForm.setWidget(1, QtGui.QFormLayout.LabelRole, self.remotePortLabel)
        self.remotePortLineEdit = QtGui.QLineEdit(NetworkDialog)
        self.remotePortLineEdit.setObjectName(_fromUtf8("remotePortLineEdit"))
        self.remoteSettingsForm.setWidget(1, QtGui.QFormLayout.FieldRole, self.remotePortLineEdit)
        self.verticalLayout.addLayout(self.remoteSettingsForm)
        self.buttonBox = QtGui.QDialogButtonBox(NetworkDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(NetworkDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NetworkDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), NetworkDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NetworkDialog)

    def retranslateUi(self, NetworkDialog):
        NetworkDialog.setWindowTitle(_translate("NetworkDialog", "Network Settings", None))
        self.remoteHostLabel.setText(_translate("NetworkDialog", "host", None))
        self.remotePortLabel.setText(_translate("NetworkDialog", "port", None))

