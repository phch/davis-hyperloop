from pyqtgraph import PlotWidget

_1m = 60

class TimePlot(PlotWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._data = []
        self._min_time = 0
        self._max_time = 0

    def update(self):
        self._max_time += 1
        if self._max_time - self._min_time > _1m:
            self._min_time = self._max_time - _1m
        self.setRange(xRange=[self._min_time, self._max_time])
