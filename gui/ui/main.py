# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Tue Jun 28 14:01:36 2016
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
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.startButton = QtGui.QCommandLinkButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.verticalLayout.addWidget(self.startButton)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.uptimeLabel = QtGui.QLabel(self.centralwidget)
        self.uptimeLabel.setObjectName(_fromUtf8("uptimeLabel"))
        self.gridLayout.addWidget(self.uptimeLabel, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.heightLCD = QtGui.QLCDNumber(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.heightLCD.sizePolicy().hasHeightForWidth())
        self.heightLCD.setSizePolicy(sizePolicy)
        self.heightLCD.setObjectName(_fromUtf8("heightLCD"))
        self.gridLayout.addWidget(self.heightLCD, 1, 1, 1, 2)
        self.velocityLabel = QtGui.QLabel(self.centralwidget)
        self.velocityLabel.setObjectName(_fromUtf8("velocityLabel"))
        self.gridLayout.addWidget(self.velocityLabel, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.heightLabel = QtGui.QLabel(self.centralwidget)
        self.heightLabel.setObjectName(_fromUtf8("heightLabel"))
        self.gridLayout.addWidget(self.heightLabel, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.velocityLCD = QtGui.QLCDNumber(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.velocityLCD.sizePolicy().hasHeightForWidth())
        self.velocityLCD.setSizePolicy(sizePolicy)
        self.velocityLCD.setObjectName(_fromUtf8("velocityLCD"))
        self.gridLayout.addWidget(self.velocityLCD, 0, 1, 1, 2)
        self.uptimeLCD = QtGui.QLCDNumber(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uptimeLCD.sizePolicy().hasHeightForWidth())
        self.uptimeLCD.setSizePolicy(sizePolicy)
        self.uptimeLCD.setObjectName(_fromUtf8("uptimeLCD"))
        self.gridLayout.addWidget(self.uptimeLCD, 2, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.networkLog = QtGui.QTextBrowser(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.networkLog.sizePolicy().hasHeightForWidth())
        self.networkLog.setSizePolicy(sizePolicy)
        self.networkLog.setObjectName(_fromUtf8("networkLog"))
        self.verticalLayout.addWidget(self.networkLog)
        self.gridLayout_2.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
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
        self.gridLayout_2.addWidget(self.tabWidget, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 588, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNetwork = QtGui.QAction(MainWindow)
        self.actionNetwork.setObjectName(_fromUtf8("actionNetwork"))
        self.menuSettings.addAction(self.actionNetwork)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Hyperloop Pod", None))
        self.startButton.setText(_translate("MainWindow", "Start", None))
        self.uptimeLabel.setText(_translate("MainWindow", "uptime", None))
        self.velocityLabel.setText(_translate("MainWindow", "velocity", None))
        self.heightLabel.setText(_translate("MainWindow", "height", None))
        self.networkLog.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.velocityTab), _translate("MainWindow", "Velocity", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.heightTab), _translate("MainWindow", "Height", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.uptimeTab), _translate("MainWindow", "Uptime", None))
        self.menuSettings.setTitle(_translate("MainWindow", "&Settings", None))
        self.actionNetwork.setText(_translate("MainWindow", "&Network", None))

