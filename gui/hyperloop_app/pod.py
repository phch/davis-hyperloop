import logging
import socket as s

BUFFER_SIZE = 2 ** 10

class UDP:
    '''UDP server

    Handles decoding of received messages.
    '''
    def __init__(self, socket):
        self._socket = socket
        self._log = logging.getLogger('udp')

    def recv(self):
        data = self._socket.recv(BUFFER_SIZE)
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

class Filter:
    def __init__(self):
        self._handlers = {}

    def add_tag(self, tag, handler):
        if tag in self._handlers:
            msg = 'tag "{}" already added'.format(tag)
            raise ValueError(msg)
        self._handlers[tag] = handler

    def filter(self, message):
        tag, payload = split(message)
        try:
            handler = self._handlers[tag]
        except KeyError as e:
            msg = 'unrecognized tag "{}" in message "{}"'
            msg = msg.format(tag, message)
            raise ValueError(msg) from e
        return handler(payload)

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

class Pod:
    '''Data and control connections to the pod'''

    def __init__(self, local_addr, remote_addr):
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
