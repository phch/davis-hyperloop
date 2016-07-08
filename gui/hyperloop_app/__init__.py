#!/usr/bin/env python3

from PyQt4.QtCore import (
    QObject,
    QTimer,
    QThread,
    pyqtSignal,
    pyqtSlot)
from PyQt4.QtGui import (
    QApplication,
    QDialog,
    QMainWindow)
from pyqtgraph.console import ConsoleWidget
from pyqtgraph import PlotWidget
import logging
import logging.config
import sys
from threading import Thread

from ui import Ui_MainWindow, Ui_NetworkDialog
from .pod import Pod
from .parser import parse_args

_1s = 1000

class MainWindow(QMainWindow):
    '''First application window the user sees'''

    command = pyqtSignal(str, str) # (tag, payload)
    networkUpdate = pyqtSignal(str, int) # (host, port)

    def __init__(self, pod):
        super().__init__()
        MainWindow.console = ConsoleWidget(
            namespace = {
                'pod': pod,
                'win': self,
            },
            text='You can use this window to enter Python commands.')
        MainWindow.console.setWindowTitle('Python interaction')
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._ui.startButton.clicked.connect(pod.begin)
        self._ui.submitButton.clicked.connect(self.submitCommand)
        pod.connected.connect(self.enable)
        self._ui.actionNetwork.triggered.connect(self.networkDialog)
        self._ui.actionConsoleOpen.triggered.connect(self.openConsole)
        pod.add_listener('*', self.appendNetworkLog)
        pod.add_listener('v', self.updateVelocityLCD)
        pod.add_listener('h', self.updateHeightLCD)
        pod.add_listener('d', self.updateDistanceLCD)
        self.command.connect(pod)
        self.networkUpdate.connect(pod.try_connect)
        self.timer = QTimer()
        self.timer.timeout.connect(self._ui.velocityPlot.update)
        self.timer.timeout.connect(self._ui.heightPlot.update)
        self.timer.timeout.connect(self._ui.distancePlot.update)
        self.timer.start(_1s)

    @pyqtSlot()
    def enable(self):
        self._ui.startButton.setDisabled(True)
        self._ui.submitButton.setDisabled(False)

    @pyqtSlot(str)
    def updateVelocityLCD(self, new):
        self._ui.velocityLCD.display(new)

    @pyqtSlot(str)
    def updateHeightLCD(self, new):
        self._ui.heightLCD.display(new)

    @pyqtSlot(str)
    def updateDistanceLCD(self, new):
        self._ui.distanceLCD.display(new)

    def submitCommand(self):
        tag = self._ui.tagLineEdit.text()
        body = self._ui.bodyLineEdit.text()
        if tag == '' or body == '':
            return
        self.command.emit(tag, body)

    def sendStartMessage(self):
        return 'start'

    def openConsole(self):
        '''Open a console for Python interaction'''
        MainWindow.console.show()

    # FIXME: The dialog is modal, so it blocks input to the network log.
    # Can we allow updates to the log while keeping modality?
    def networkDialog(self):
        '''Open a window for changing network settings'''
        dialog = NetworkDialog()
        if dialog.exec_() == QDialog.Accepted:
            self.networkUpdate.emit(dialog.host, dialog.port)

    @pyqtSlot(str)
    def appendNetworkLog(self, text):
        self._ui.networkLog.appendPlainText(text)

class NetworkDialog(QDialog):
    '''Dialog window where the user can change hosts and ports'''

    def __init__(self):
        super().__init__()
        self.host = None
        self.port = None
        self._ui = Ui_NetworkDialog()
        self._ui.setupUi(self)

    def accept(self):
        '''Handle the user clicking OK'''
        # TODO: validate input
        self.host = self._ui.remoteHostLineEdit.text()
        self.port = self._ui.remotePortLineEdit.text()
        self.port = int(self.port)
        super().accept() # closes the window

def setup_logging(level):
    logging.config.fileConfig(
        'logging.conf',
        defaults={'verbosity': logging.getLevelName(level)}
    )

def remote_addr(args):
    host = args.host
    if host == 'localhost':
        host = '127.0.0.1'
    port = int(args.port)
    return (host, port)

def main():
    app = QApplication(sys.argv)

    args = sys.argv[1:]
    args = parse_args(args)
    setup_logging(int(args.log) * 10)

    host, port = remote_addr(args)
    pod = Pod(host, port)
    win = MainWindow(pod)

    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
