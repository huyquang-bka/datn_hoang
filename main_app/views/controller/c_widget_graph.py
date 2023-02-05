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
        self.styles = {'color': 'red', 'font-size': '20pt'}
        self.graph.setTitle("Graph of people estimate", color="r", size="20pt")
        self.graph.setLabel("left", "People estimate", **self.styles)
        self.graph.setLabel("bottom", "Time", **self.styles)
        self.graph.addLegend()
        self.list_x = deque(maxlen=10)
        self.list_y = deque(maxlen=10)
        
    def stop(self):
        self.list_x.clear()
        self.list_y.clear()
        self.graph.clear()
        
    def slot_graph(self, data):
        self.graph.clear()
        y, x = data
        self.list_x.append(x)
        self.list_y.append(y)
        x_labels = [(index, label) for index, label in enumerate(self.list_x)]
        x_indexs = [index for index, label in enumerate(self.list_x)]
        self.graph.plot(x_indexs, self.list_y, symbol='o', symbolSize=10, symbolBrush='g', pen='r', name="People estimate", labels=x_labels)
        ax=self.graph.getAxis('bottom')
        ax.setTicks([x_labels])
        
    def resizeEvent(self, e):
        super().resizeEvent(e)
        self.graph.resize(self.width(), self.height())
        self.graph.move(0, 0)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = WidgetGraph()
    window.show()
    sys.exit(app.exec_())