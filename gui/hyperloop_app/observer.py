import weakref

"""
Mostly taken from https://github.com/DanielSank/observed
"""

class CleanupHandler:
    def __init__(self, key, table):
        self._key = key
        self._table = table

    def __call__(self, ref):
        self._table.pop(self._key, None)

class Subject:
    def __init__(self):
        self._observers = {}

    def register(self, observer):
        key = id(observer)
        if key in self._observers:
            return
        callback = CleanupHandler(key, self._observers)
        ref = weakref.ref(observer, callback)
        self._observers[key] = ref

    def deregister(self, observer):
        key = id(observer)
        if key in self._observers:
            del self._observers[key]

    def notify(self, message):
        for observer in self._observers.values():
            observer()(message)
