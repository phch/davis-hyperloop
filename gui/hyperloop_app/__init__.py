#!/usr/bin/env python3

from PyQt4.QtCore import QThread, pyqtSlot
from PyQt4.QtGui import (
    QApplication,
    QDialog,
    QMainWindow,
)
import logging
import logging.config
import sys
from threading import Thread

from ui import Ui_MainWindow, Ui_NetworkDialog
from .pod import Pod
from .parser import parse_args

class MainWindow(QMainWindow):
    '''First application window the user sees'''

    def __init__(self, pod):
        super().__init__()
        self._pod = pod
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._ui.actionNetwork.triggered.connect(self.networkDialog)
        pod.add_listener("*", self.appendNetworkLog)

    def networkDialog(self):
        '''Open a window for changing network settings'''
        la = self._pod.get_local_addr()
        ra = self._pod.get_remote_addr()
        info = NetworkInfo(local=la, remote=ra)
        dialog = NetworkDialog(info)
        if dialog.exec_() == QDialog.Accepted:
            la, old = info.local, la
            if la != old:
                self._pod.set_local_addr(info.local)
            ra, old = info.remote, ra
            if ra != old:
                self._pod.set_remote_addr(info.remote)

    @pyqtSlot(str)
    def appendNetworkLog(self, text):
        self._ui.networkLog.appendPlainText(text)

# Give this, not the whole pod, to NetworkDialog.
class NetworkInfo:
    def __init__(self, local, remote):
        self.local = local
        self.remote = remote

class NetworkDialog(QDialog):
    '''Dialog window where the user can change hosts and ports'''

    def __init__(self, info):
        super().__init__()
        self._info = info
        self._ui = Ui_NetworkDialog()
        self._ui.setupUi(self)
        (lh, lp) = self._info.local
        self._ui.localHostLineEdit.setText(lh)
        self._ui.localPortLineEdit.setText(str(lp))
        (rh, rp) = self._info.remote
        self._ui.remoteHostLineEdit.setText(rh)
        self._ui.remotePortLineEdit.setText(str(rp))

    def accept(self):
        '''Handle the user clicking OK'''
        # TODO: validate input
        lh = self._ui.localHostLineEdit.text()
        lp = self._ui.localPortLineEdit.text()
        self._info.local = (lh, int(lp))
        rh = self._ui.remoteHostLineEdit.text()
        rp = self._ui.remotePortLineEdit.text()
        self._info.remote = (rh, int(rp))
        super().accept() # closes the window

def setup_logging(level):
    logging.config.fileConfig(
        'logging.conf',
        defaults={'verbosity': logging.getLevelName(level)}
    )

def local_addr(args):
    host = 'localhost'
    port = int(args.local_udp_port)
    return (host, port)

def remote_addr(args):
    host = args.remote_tcp_host
    port = int(args.remote_tcp_port)
    return (host, port)

def main():
    app = QApplication(sys.argv)

    args = sys.argv[1:]
    args = parse_args(args)
    setup_logging(int(args.log) * 10)

    la = local_addr(args)
    ra = remote_addr(args)
    pod = Pod(la, ra)
    win = MainWindow(pod)

    t = QThread()
    t.started.connect(pod.loop)
    t.finished.connect(pod.halt)
    app.lastWindowClosed.connect(t.quit)
    pod.moveToThread(t)

    win.show()
    t.start()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
