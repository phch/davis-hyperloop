#!/usr/bin/env python3

from PyQt4 import QtGui
import argparse
import logging
import logging.config
import socket
import sys
from ui import Ui_MainWindow

parser = argparse.ArgumentParser()
parser.add_argument(
    'ip', metavar='IP', help='IP address of the pod',
)
parser.add_argument(
    'port', metavar='PORT', help='port of the pod',
)
parser.add_argument(
    '--log', metavar='LEVEL', help='logging level',
    choices=list('12345'), default=2, # INFO default
)
parser.add_argument(
    '--source', metavar='SOURCE_IP', help='source IP address',
    default=8880,
)

def parse_args(args):
    return parser.parse_args(args=args)

class MainWindow(QtGui.QMainWindow):
    def __init__(self, pod):
        QtGui.QMainWindow.__init__(self)
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self) # must come before other configuration
        self._ui.pingButton.clicked.connect(lambda: pod.ping())
        # TODO: The two below lines smell.
        self._ui.ipLineEdit.setText(pod._udp._ip)
        self._ui.portLineEdit.setText(str(pod._udp._port))
        self.setWindowTitle('Hyperloop pod')

class Udp(object):
    def __init__(self, ip, port, source):
        self._ip = ip
        self._port = port
        self._source = source
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._sock.bind(('', source))
        self._sock.settimeout(1e-2)
        self._log = logging.getLogger('pod.udp')
        self._log.debug('UDP socket bound')

    def send(self, message):
        data = None
        try:
            self._sock.sendto(bytes(message, 'UTF-8'), (self._ip, self._port))
            data, _ = self._sock.recvfrom(1024)
        except socket.timeout:
            self._log.warning('socket timeout')
        except socket.error as e:
            # TODO: do something more informative
            self._log.error(e)
            sys.exit(1)
        return data

class Pod(object):
    def __init__(self, udp):
        self._udp = udp
        self._log = logging.getLogger('pod')
        self._log.debug('setup complete')

    def ping(self):
        self._log.debug('ping')
        self._udp.send('ping')

def main():
    args = sys.argv[1:]
    args = parse_args(args)
    UDP_IP = args.ip
    UDP_PORT = int(args.port)
    SOURCE_IP = args.source
    loglevel = int(args.log) * 10
    logging.config.fileConfig(
        'logging.conf',
        defaults={'verbosity': logging.getLevelName(loglevel)}
    )
    udp = Udp(UDP_IP, UDP_PORT, SOURCE_IP)
    pod = Pod(udp)
    app = QtGui.QApplication(sys.argv)
    win = MainWindow(pod)
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
