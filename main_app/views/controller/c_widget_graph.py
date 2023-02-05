import time
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
from collections import deque


class WidgetGraph(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.graph = pg.PlotWidget(self, background="w")
        self.graph.resize(self.width(), self.height())
        self.styles = {'color': 'w', 'font-size': '20pt'}
        self.graph.setTitle("Graph of people estimate", color="r", size="20pt")
        self.graph.setLabel("left", "People estimate", **self.styles)
        self.graph.addLegend()
        self.list_x = deque(maxlen=10)
        self.list_y = deque(maxlen=10)
        
    def slot_graph(self, data):
        self.graph.clear()
        y, x = data
        self.list_x.append(x)
        self.list_y.append(y)
        x_dict = dict(enumerate(self.list_x))
        # self.graph.plot(self.list_x, self.list_y, symbol='o', symbolSize=10, symbolBrush='g', pen='r')
        stringaxis = pg.AxisItem(orientation='bottom')
        stringaxis.setTicks([x_dict.items()])
        self.graph.setAxisItems(axisItems = {'bottom': stringaxis})
        self.graph.setLabel("bottom", "Time", **self.styles)
        self.graph.plot(list(x_dict.keys()), self.list_y, symbol='o', symbolSize=10, symbolBrush='g', pen='r', name="People estimate")
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = WidgetGraph()
    window.show()
    sys.exit(app.exec_())