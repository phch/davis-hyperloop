from collections import defaultdict
from PyQt4.QtNetwork import (
    QHostAddress,
    QTcpSocket,
    QUdpSocket,
)
from PyQt4.QtCore import (
    QEventLoop,
    QObject,
    QThread,
    pyqtSignal,
    pyqtSlot,
)
from PyQt4.QtGui import QApplication

import logging
import socket as s
import time

BUFFER_SIZE = 2 ** 10

def query_tag(tag, *subtags):
    tag = '?' + tag
    if subtags:
        tag += '.' + '.'.join(subtags)
    return tag

def reply_tag(tag, *subtags):
    tag = '!' + tag
    if subtags:
        tag += '.' + '.'.join(subtags)
    return tag

def randport():
    from random import randrange
    return randrange(8000, 9000)

def bind(sock, tries=3):
    from itertools import repeat
    host = QHostAddress.LocalHost
    for _ in repeat(None, tries):
        port = randport()
        if sock.bind(host, port):
            return True
    return False

def split(message):
    try:
        tag, payload = message.split(':', 1)
    except ValueError as e: # no colon
        msg = 'no tag separator in message "{}"'.format(message)
        raise ValueError(msg) from e
    return tag, payload

class Messager(QObject):
    received = pyqtSignal(str)

    def connect(self, slot):
        self.received.connect(slot)

    def emit(self, message):
        self.received.emit(message)

@pyqtSlot(str)
class Filter:
    def __init__(self):
        self._messagers = defaultdict(Messager)
        self._unfiltered = Messager()

    def __call__(self, message):
        self._unfiltered.emit(message)
        tag, payload = split(message)
        self._messagers[tag].emit(payload)

    def add_listener(self, tag, slot):
        if tag == '*':
            messager = self._unfiltered
        else:
            messager = self._messagers[tag]
        messager.connect(slot)

class UdpServer(QObject):
    datagram = pyqtSignal(str)

    def __init__(self, host):
        super().__init__()
        self._sock = QUdpSocket()
        self._host = host
        self._sock.readyRead.connect(self.recv)
        bind(self._sock)

    def set_host(self, host):
        self._host = host

    @pyqtSlot(str)
    def try_connect(self, port):
        port = int(port)
        self._sock.writeDatagram('_:start\n', self._host, port)

    def recv(self):
        while self._sock.hasPendingDatagrams():
            data, _, _ = self._sock.readDatagram(BUFFER_SIZE)
            message = data.decode()
            self.datagram.emit(message)

class TcpClient(QObject):
    packet = pyqtSignal(str)
    connected = pyqtSignal()
    disconnected = pyqtSignal()

    def __init__(self, host):
        super().__init__()
        self._sock = QTcpSocket()
        self._host = host
        self._log = logging.getLogger('tcp')
        self._sock.connected.connect(self.greet)
        self._sock.connected.connect(self.connected.emit)
        self._sock.disconnected.connect(self.disconnected.emit)
        self._sock.readyRead.connect(self.recv)

    def set_host(self, host):
        self._sock.disconnectFromHost()
        self._host = host

    def try_connect(self, port):
        msg = 'connecting to ({}:{})'
        msg = msg.format(self._host.toString(), port)
        self._log.debug(msg)
        self._sock.connectToHost(self._host, port)
        ok = self._sock.waitForConnected()
        if not ok:
            self._log.error('failed to connect')
        self._log.debug('connection successful')

    def greet(self):
        self.send(query_tag('port', 'udp'), '')

    def recv(self):
        while self._sock.canReadLine():
            data = bytes(self._sock.readLine()) # handle QByteArray
            message = data.decode()
            self.packet.emit(message)

    def send(self, tag, payload):
        message = tag + ':' + payload + '\n'
        data = message.encode()
        self._sock.write(data)

@pyqtSlot(str, str) # (tag, payload)
class Pod(QObject):
    '''Data and control connections to the pod'''

    connected = pyqtSignal()

    def __init__(self, host, port):
        super().__init__()
        self._host = QHostAddress(host)
        self._port = port
        self._log = logging.getLogger('pod')
        self._tcp = TcpClient(self._host)
        self._udp = UdpServer(self._host)
        self._filter = Filter()
        self._tcp.packet.connect(self._filter)
        self._tcp.connected.connect(self.connected.emit)
        self._udp.datagram.connect(self._filter)
        self.add_listener(
            reply_tag('port', 'udp'),
            self._udp.try_connect)

    def __call__(self, tag, payload):
        self._tcp.send(tag, payload)

    @pyqtSlot()
    def begin(self):
        self._tcp.try_connect(self._port)

    @pyqtSlot(str, int)
    def try_connect(self, host, port):
        if host == 'localhost':
            host = '127.0.0.1'
        host = QHostAddress(host)
        if host != self._host:
            self._tcp.set_host(host)
            self._udp.set_host(host)
            self._host = host
        self._port = port
        self.begin()

    def add_listener(self, tag, listener):
        self._filter.add_listener(tag, listener)
