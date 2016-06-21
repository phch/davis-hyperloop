# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'network_dialog.ui'
#
# Created: Tue Jun 21 13:33:14 2016
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
        NetworkDialog.resize(400, 237)
        self.verticalLayout = QtGui.QVBoxLayout(NetworkDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.localSettingsBox = QtGui.QGroupBox(NetworkDialog)
        self.localSettingsBox.setObjectName(_fromUtf8("localSettingsBox"))
        self.gridLayout = QtGui.QGridLayout(self.localSettingsBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.localSettingsForm = QtGui.QFormLayout()
        self.localSettingsForm.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.localSettingsForm.setObjectName(_fromUtf8("localSettingsForm"))
        self.localHostLabel = QtGui.QLabel(self.localSettingsBox)
        self.localHostLabel.setObjectName(_fromUtf8("localHostLabel"))
        self.localSettingsForm.setWidget(0, QtGui.QFormLayout.LabelRole, self.localHostLabel)
        self.localHostLineEdit = QtGui.QLineEdit(self.localSettingsBox)
        self.localHostLineEdit.setObjectName(_fromUtf8("localHostLineEdit"))
        self.localSettingsForm.setWidget(0, QtGui.QFormLayout.FieldRole, self.localHostLineEdit)
        self.localPortLabel = QtGui.QLabel(self.localSettingsBox)
        self.localPortLabel.setObjectName(_fromUtf8("localPortLabel"))
        self.localSettingsForm.setWidget(1, QtGui.QFormLayout.LabelRole, self.localPortLabel)
        self.localPortLineEdit = QtGui.QLineEdit(self.localSettingsBox)
        self.localPortLineEdit.setObjectName(_fromUtf8("localPortLineEdit"))
        self.localSettingsForm.setWidget(1, QtGui.QFormLayout.FieldRole, self.localPortLineEdit)
        self.gridLayout.addLayout(self.localSettingsForm, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.localSettingsBox)
        self.remoteSettingsBox = QtGui.QGroupBox(NetworkDialog)
        self.remoteSettingsBox.setObjectName(_fromUtf8("remoteSettingsBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.remoteSettingsBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.remoteSettingsForm = QtGui.QFormLayout()
        self.remoteSettingsForm.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.remoteSettingsForm.setObjectName(_fromUtf8("remoteSettingsForm"))
        self.remoteHostLabel = QtGui.QLabel(self.remoteSettingsBox)
        self.remoteHostLabel.setObjectName(_fromUtf8("remoteHostLabel"))
        self.remoteSettingsForm.setWidget(0, QtGui.QFormLayout.LabelRole, self.remoteHostLabel)
        self.remoteHostLineEdit = QtGui.QLineEdit(self.remoteSettingsBox)
        self.remoteHostLineEdit.setObjectName(_fromUtf8("remoteHostLineEdit"))
        self.remoteSettingsForm.setWidget(0, QtGui.QFormLayout.FieldRole, self.remoteHostLineEdit)
        self.remotePortLabel = QtGui.QLabel(self.remoteSettingsBox)
        self.remotePortLabel.setObjectName(_fromUtf8("remotePortLabel"))
        self.remoteSettingsForm.setWidget(1, QtGui.QFormLayout.LabelRole, self.remotePortLabel)
        self.remotePortLineEdit = QtGui.QLineEdit(self.remoteSettingsBox)
        self.remotePortLineEdit.setObjectName(_fromUtf8("remotePortLineEdit"))
        self.remoteSettingsForm.setWidget(1, QtGui.QFormLayout.FieldRole, self.remotePortLineEdit)
        self.gridLayout_2.addLayout(self.remoteSettingsForm, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.remoteSettingsBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
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
        self.localSettingsBox.setTitle(_translate("NetworkDialog", "Local", None))
        self.localHostLabel.setText(_translate("NetworkDialog", "host", None))
        self.localPortLabel.setText(_translate("NetworkDialog", "port", None))
        self.remoteSettingsBox.setTitle(_translate("NetworkDialog", "Remote", None))
        self.remoteHostLabel.setText(_translate("NetworkDialog", "host", None))
        self.remotePortLabel.setText(_translate("NetworkDialog", "port", None))

