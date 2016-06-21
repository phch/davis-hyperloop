from asyncio import DatagramProtocol, Protocol
from logging import getLogger
import socket

from .observer import Subject

class DataStream(Subject, DatagramProtocol):
    def __init__(self):
        super().__init__()
        self._paused = False
        self._log = getLogger('udp')

    def connection_made(self, transport):
        host, port = transport._sock.getsockname()
        output = 'connection made ({}:{})'.format(host, port)
        self._log.debug(output)

    def connection_lost(self, exc):
        normal = 'EOF received or connection aborted or closed'
        output = 'connection lost ({})'.format(exc or normal)
        self._log.debug(output)

    def datagram_received(self, data, addr):
        message = data.decode()
        (host, port) = addr
        output = 'received "{}" ({}:{})'.format(message, host, port)
        self._log.debug(output)
        if not self._paused:
            self.notify(message)

    def pause(self):
        self._paused = True
        self._log.debug('paused')

    def resume(self):
        self._paused = False
        self._log.debug('resumed')

# @asyncio.coroutine
# def open_data_stream(loop=None, **kwargs):
#     if loop is None:
#         loop = asyncio.get_event_loop()
#     _, protocol = yield from loop.create_datagram_endpoint(
#         DataStream, **kwargs)
#     return protocol

class ControlStream(Subject, Protocol):
    def __init__(self):
        super().__init__()
        self._log = getLogger('tcp')

    def connection_made(self, transport):
        host, port = transport._sock.getsockname()
        output = 'connection made ({}:{})'.format(host, port)
        self._log.debug(output)

    def connection_lost(self, exc):
        normal = 'EOF received or connection aborted or closed'
        output = 'connection lost ({})'.format(exc or normal)
        self._log.debug(output)

    def data_received(self, data):
        message = data.decode()
        (host, port) = addr
        output = 'received "{}" ({}:{})'.format(message, host, port)
        self._log.debug(output)
        if not self._paused:
            self.notify(message)


# TODO: Do something like this for UDP and TCP connections:

class Supervisor:
    def __init__(self, connection):
        self._connection = connection

    def run(self):
        while True:
            while self._connection.ok():
                pass
            self._connection.restart()

class UDP:
    def restart(self):
        pass

    def ok(self):
        return False
