from collections import defaultdict
from PyQt4.QtCore import QEventLoop, QObject, QThread, pyqtSignal
from PyQt4.QtGui import QApplication

import logging
import socket as s
import time

BUFFER_SIZE = 2 ** 10

# TODO: Use QUdpSocket?
class UDP:
    '''UDP server

    Handles decoding of received messages.
    '''
    def __init__(self, socket):
        self._socket = socket
        self._log = logging.getLogger('udp')

    def recv(self):
        try:
            data = self._socket.recv(BUFFER_SIZE)
        except OSError:
            return None
        message = data.decode()
        return message

    def close(self):
        self._socket.close()

def split(message):
    try:
        tag, payload = message.split(':', 1)
    except ValueError as e: # no colon
        msg = 'no tag separator in message "{}"'.format(message)
        raise ValueError(msg) from e
    return tag, payload

class Messager(QObject):
    trigger = pyqtSignal(str)

    def connect(self, slot):
        self.trigger.connect(slot)

    def emit(self, message):
        self.trigger.emit(message)

class Filter:
    def __init__(self):
        self._messagers = defaultdict(Messager)
        self._unfiltered = Messager()

    def add_listener(self, tag, slot):
        if tag == '*':
            messager = self._unfiltered
        else:
            messager = self._messagers[tag]
        messager.connect(slot)

    def filter(self, message):
        tag, payload = split(message)
        self._unfiltered.emit(payload)
        self._messagers[tag].emit(payload)

# Superclass for DataStream and ControlStream.  Implements some of their
# common functionality.
class Stream:
    def __init__(self):
        self._host = None
        self._port = None
        self._exn = None

    def get_error(self):
        return self._exn

    def get_addr(self):
        return (self._host, self._port)

    def set_addr(self, addr):
        self._host, self._port = addr
        self.connect()

class DataStream(Stream):
    '''Connection for getting data from the pod'''

    def __init__(self, local_addr):
        super().__init__()
        self._host, self._port = local_addr
        self._filter = Filter()
        self._log = logging.getLogger('data')
        self._udp = None
        self.connect()

    def connect(self):
        msg = 'Connecting to {}:{}'.format(self._host, self._port)
        self._log.debug(msg)
        try:
            sock = s.socket(s.AF_INET, s.SOCK_DGRAM)
            sock.setblocking(False)
            sock.bind((self._host, self._port))
            if self._udp:
                self._udp.close()
            self._udp = UDP(sock)
        except OSError as e:
            self._log.error(e)
            self._udp = None
            self._exn = e
        else:
            self._exn = None

    def add_listener(self, tag, slot):
        self._filter.add_listener(tag, slot)

    def recv(self):
        message = self._udp.recv()
        if message is None:
            return
        try:
            self._filter.filter(message)
        except ValueError as e:
            self._log.error(e)

# TODO: Use QTcpSocket?
class TCP:
    '''TCP client

    Handles encoding of sent messages.
    '''

    def __init__(self, socket):
        self._socket = socket
        self._log = logging.getLogger('tcp')

    def send(self, message):
        data = message.encode()
        self._socket.send(data)

    def close(self):
        self._socket.close()

class ControlStream(Stream):
    '''Connection for sending commands to the pod'''

    def __init__(self, remote_addr):
        self._host, self._port = remote_addr
        self._log = logging.getLogger('control')
        self._tcp = None
        self.connect()

    def connect(self):
        msg = 'Connecting to {}:{}'.format(self._host, self._port)
        self._log.debug(msg)
        try:
            sock = s.socket(s.AF_INET, s.SOCK_STREAM)
            sock.connect((self._host, self._port))
            if self._tcp:
                self._tcp.close()
            self._tcp = TCP(sock)
        except OSError as e:
            self._log.error(e)
            self._tcp = None
            self._exn = e
        else:
            self._exn = None

    def send(message):
        self._tcp.send(message)

class Pod(QObject):
    '''Data and control connections to the pod'''

    def __init__(self, local_addr, remote_addr):
        super().__init__()
        self._running = False
        self._ds = DataStream(local_addr)
        self._cs = ControlStream(remote_addr)
        self._log = logging.getLogger('pod')

    def get_local_addr(self):
        return self._ds.get_addr()

    def set_local_addr(self, addr):
        self._ds.set_addr(addr)

    def get_remote_addr(self):
        return self._cs.get_addr()

    def set_remote_addr(self, addr):
        self._cs.set_addr(addr)

    def add_controller(self, controller):
        pass # TODO

    def add_listener(self, tag, listener):
        self._ds.add_listener(tag, listener)

    def loop(self):
        self._running = True
        while self._running:
            self._ds.recv()
            QApplication.processEvents() # prevents sluggish UI

    def halt(self):
        old = self._running
        self._running = False
        return old
