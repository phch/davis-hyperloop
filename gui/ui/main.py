# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Fri Jul  1 14:45:20 2016
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
        MainWindow.resize(588, 500)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.leftColumn = QtGui.QVBoxLayout()
        self.leftColumn.setObjectName(_fromUtf8("leftColumn"))
        self.mainButtonLayout = QtGui.QHBoxLayout()
        self.mainButtonLayout.setObjectName(_fromUtf8("mainButtonLayout"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setAutoExclusive(False)
        self.startButton.setDefault(True)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.buttonGroup = QtGui.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.startButton)
        self.mainButtonLayout.addWidget(self.startButton)
        self.pauseButton = QtGui.QPushButton(self.centralwidget)
        self.pauseButton.setEnabled(False)
        self.pauseButton.setAutoDefault(False)
        self.pauseButton.setDefault(False)
        self.pauseButton.setFlat(False)
        self.pauseButton.setObjectName(_fromUtf8("pauseButton"))
        self.buttonGroup.addButton(self.pauseButton)
        self.mainButtonLayout.addWidget(self.pauseButton)
        self.leftColumn.addLayout(self.mainButtonLayout)
        self.commandBox = QtGui.QGroupBox(self.centralwidget)
        self.commandBox.setObjectName(_fromUtf8("commandBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.commandBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.commandForm = QtGui.QFormLayout()
        self.commandForm.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.commandForm.setObjectName(_fromUtf8("commandForm"))
        self.tagLabel = QtGui.QLabel(self.commandBox)
        self.tagLabel.setObjectName(_fromUtf8("tagLabel"))
        self.commandForm.setWidget(0, QtGui.QFormLayout.LabelRole, self.tagLabel)
        self.tagLineEdit = QtGui.QLineEdit(self.commandBox)
        self.tagLineEdit.setMaxLength(10)
        self.tagLineEdit.setObjectName(_fromUtf8("tagLineEdit"))
        self.commandForm.setWidget(0, QtGui.QFormLayout.FieldRole, self.tagLineEdit)
        self.bodyLabel = QtGui.QLabel(self.commandBox)
        self.bodyLabel.setObjectName(_fromUtf8("bodyLabel"))
        self.commandForm.setWidget(1, QtGui.QFormLayout.LabelRole, self.bodyLabel)
        self.bodyLineEdit = QtGui.QLineEdit(self.commandBox)
        self.bodyLineEdit.setMaxLength(50)
        self.bodyLineEdit.setObjectName(_fromUtf8("bodyLineEdit"))
        self.commandForm.setWidget(1, QtGui.QFormLayout.FieldRole, self.bodyLineEdit)
        self.verticalLayout.addLayout(self.commandForm)
        self.pushButton = QtGui.QPushButton(self.commandBox)
        self.pushButton.setEnabled(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.leftColumn.addWidget(self.commandBox)
        self.networkLog = QtGui.QPlainTextEdit(self.centralwidget)
        self.networkLog.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.networkLog.setMaximumBlockCount(50)
        self.networkLog.setCenterOnScroll(False)
        self.networkLog.setObjectName(_fromUtf8("networkLog"))
        self.leftColumn.addWidget(self.networkLog)
        self.leftColumn.setStretch(2, 1)
        self.horizontalLayout.addLayout(self.leftColumn)
        self.rightColumn = QtGui.QVBoxLayout()
        self.rightColumn.setObjectName(_fromUtf8("rightColumn"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(350, 0))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.velocityTab = QtGui.QWidget()
        self.velocityTab.setObjectName(_fromUtf8("velocityTab"))
        self.tabWidget.addTab(self.velocityTab, _fromUtf8(""))
        self.heightTab = QtGui.QWidget()
        self.heightTab.setObjectName(_fromUtf8("heightTab"))
        self.tabWidget.addTab(self.heightTab, _fromUtf8(""))
        self.uptimeTab = QtGui.QWidget()
        self.uptimeTab.setObjectName(_fromUtf8("uptimeTab"))
        self.tabWidget.addTab(self.uptimeTab, _fromUtf8(""))
        self.distanceTab = QtGui.QWidget()
        self.distanceTab.setObjectName(_fromUtf8("distanceTab"))
        self.tabWidget.addTab(self.distanceTab, _fromUtf8(""))
        self.rightColumn.addWidget(self.tabWidget)
        self.summaryBox = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.summaryBox.sizePolicy().hasHeightForWidth())
        self.summaryBox.setSizePolicy(sizePolicy)
        self.summaryBox.setObjectName(_fromUtf8("summaryBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.summaryBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.velocityLabel = QtGui.QLabel(self.summaryBox)
        self.velocityLabel.setObjectName(_fromUtf8("velocityLabel"))
        self.gridLayout_2.addWidget(self.velocityLabel, 0, 0, 1, 1)
        self.velocityLCD = QtGui.QLCDNumber(self.summaryBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.velocityLCD.sizePolicy().hasHeightForWidth())
        self.velocityLCD.setSizePolicy(sizePolicy)
        self.velocityLCD.setNumDigits(10)
        self.velocityLCD.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.velocityLCD.setObjectName(_fromUtf8("velocityLCD"))
        self.gridLayout_2.addWidget(self.velocityLCD, 0, 1, 1, 1)
        self.uptimeLCD = QtGui.QLCDNumber(self.summaryBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uptimeLCD.sizePolicy().hasHeightForWidth())
        self.uptimeLCD.setSizePolicy(sizePolicy)
        self.uptimeLCD.setNumDigits(10)
        self.uptimeLCD.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.uptimeLCD.setObjectName(_fromUtf8("uptimeLCD"))
        self.gridLayout_2.addWidget(self.uptimeLCD, 2, 1, 1, 1)
        self.heightLCD = QtGui.QLCDNumber(self.summaryBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.heightLCD.sizePolicy().hasHeightForWidth())
        self.heightLCD.setSizePolicy(sizePolicy)
        self.heightLCD.setNumDigits(10)
        self.heightLCD.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.heightLCD.setObjectName(_fromUtf8("heightLCD"))
        self.gridLayout_2.addWidget(self.heightLCD, 1, 1, 1, 1)
        self.uptimeLabel = QtGui.QLabel(self.summaryBox)
        self.uptimeLabel.setObjectName(_fromUtf8("uptimeLabel"))
        self.gridLayout_2.addWidget(self.uptimeLabel, 2, 0, 1, 1)
        self.heightLabel = QtGui.QLabel(self.summaryBox)
        self.heightLabel.setObjectName(_fromUtf8("heightLabel"))
        self.gridLayout_2.addWidget(self.heightLabel, 1, 0, 1, 1)
        self.distanceLabel = QtGui.QLabel(self.summaryBox)
        self.distanceLabel.setObjectName(_fromUtf8("distanceLabel"))
        self.gridLayout_2.addWidget(self.distanceLabel, 3, 0, 1, 1)
        self.distanceLCD = QtGui.QLCDNumber(self.summaryBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.distanceLCD.sizePolicy().hasHeightForWidth())
        self.distanceLCD.setSizePolicy(sizePolicy)
        self.distanceLCD.setSmallDecimalPoint(False)
        self.distanceLCD.setNumDigits(10)
        self.distanceLCD.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.distanceLCD.setObjectName(_fromUtf8("distanceLCD"))
        self.gridLayout_2.addWidget(self.distanceLCD, 3, 1, 1, 1)
        self.rightColumn.addWidget(self.summaryBox)
        self.rightColumn.setStretch(0, 2)
        self.horizontalLayout.addLayout(self.rightColumn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 588, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuConsole = QtGui.QMenu(self.menubar)
        self.menuConsole.setObjectName(_fromUtf8("menuConsole"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNetwork = QtGui.QAction(MainWindow)
        self.actionNetwork.setObjectName(_fromUtf8("actionNetwork"))
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionConsoleOpen = QtGui.QAction(MainWindow)
        self.actionConsoleOpen.setObjectName(_fromUtf8("actionConsoleOpen"))
        self.menuSettings.addAction(self.actionNetwork)
        self.menuConsole.addAction(self.actionConsoleOpen)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuConsole.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Hyperloop Pod", None))
        self.startButton.setText(_translate("MainWindow", "Begin Interaction", None))
        self.pauseButton.setText(_translate("MainWindow", "Idle Mode", None))
        self.commandBox.setTitle(_translate("MainWindow", "Send a command", None))
        self.tagLabel.setText(_translate("MainWindow", "tag", None))
        self.bodyLabel.setText(_translate("MainWindow", "body", None))
        self.pushButton.setText(_translate("MainWindow", "Submit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.velocityTab), _translate("MainWindow", "Velocity", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.heightTab), _translate("MainWindow", "Height", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.uptimeTab), _translate("MainWindow", "Uptime", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.distanceTab), _translate("MainWindow", "Distance", None))
        self.summaryBox.setTitle(_translate("MainWindow", "Summary", None))
        self.velocityLabel.setText(_translate("MainWindow", "velocity", None))
        self.uptimeLabel.setText(_translate("MainWindow", "uptime", None))
        self.heightLabel.setText(_translate("MainWindow", "height", None))
        self.distanceLabel.setText(_translate("MainWindow", "distance", None))
        self.menuSettings.setTitle(_translate("MainWindow", "&Settings", None))
        self.menuConsole.setTitle(_translate("MainWindow", "&Console", None))
        self.actionNetwork.setText(_translate("MainWindow", "&Network", None))
        self.actionNew.setText(_translate("MainWindow", "&New", None))
        self.actionConsoleOpen.setText(_translate("MainWindow", "&Open", None))

