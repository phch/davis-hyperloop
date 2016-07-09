from pyqtgraph import PlotWidget
from PyQt4.QtCore import pyqtSignal, pyqtSlot

class TimePlot(PlotWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._max_range = 60 # 1 minute
        self._xs = []
        self._ys = []
        self._next = None # y coordinate to be added
        self._secs = 0
        self._curve = self.plot()

    @pyqtSlot()
    def update(self):
        self._secs += 1
        if self._next:
            self._xs.append(self._secs)
            self._ys.append(self._next)
            self._next = None
        if len(self._xs) > self._max_range:
            self._xs.pop(0)
            self._ys.pop(0)
        xmin = max(0, self._secs - self._max_range)
        xmax = self._secs
        self.setRange(xRange=[xmin, xmax])
        self._curve.setData(self._xs, self._ys)

    @pyqtSlot(str)
    def datum(self, string):
        self._next = float(string)
