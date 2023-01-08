import cv2
from ..ui.widget_draw import Ui_WidgetDraw
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5 import QtGui, QtCore


class LabelImage(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setScaledContents(True)
        self.frame = None
        self.top_left = None
        self.bottom_right = None
        self.bottom_right_move = None
    
    def mousePressEvent(self, event: QtGui.QMouseEvent):
        if event.button() == QtCore.Qt.LeftButton:
            self.bottom_right = None
            self.bottom_right_move = None
            self.top_left = (event.pos().x(), event.pos().y())
        self.update()
    
    def mouseMoveEvent(self, event):
        self.bottom_right_move = (event.pos().x(), event.pos().y())
        self.update()
    
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.bottom_right = (event.pos().x(), event.pos().y())
        self.update()
    
    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        if self.frame is not None:
            self.show_image(self.frame, qp)
        qp.setPen(QtGui.QPen(QtCore.Qt.red, 2, QtCore.Qt.SolidLine))
        if self.bottom_right is not None:
            x1, y1 = self.top_left
            x2, y2 = self.bottom_right
            qp.drawRect(QtCore.QRect(x1, y1, x2 - x1, y2 - y1))
        elif self.bottom_right_move is not None and self.top_left is not None:
            x1, y1 = self.top_left
            x2, y2 = self.bottom_right_move
            qp.drawRect(QtCore.QRect(x1, y1, x2 - x1, y2 - y1))
        self.update()
        
    def show_image(self, rgb_img, painter: QtGui.QPainter):
        qt_img = QtGui.QPixmap.fromImage(
            QtGui.QImage(rgb_img.data, rgb_img.shape[1], rgb_img.shape[0], QtGui.QImage.Format_RGB888)).scaled(
            self.width(), self.height())
        painter.drawPixmap(self.rect(), qt_img)
        

class WidgetDraw(QWidget):
    sig_roi = QtCore.pyqtSignal(tuple)
    def __init__(self):
        super().__init__()
        self.ui = Ui_WidgetDraw()
        self.ui.setupUi(self)
        self.setMouseTracking(True)
                
        self.ui.qlabel_frame = LabelImage(self)
        self.ui.gridLayout.addWidget(self.ui.qlabel_frame, 0, 0, 1, 1)

        self.setWindowTitle("Draw Region of Interest")
        
        self.connect_button_signal()
                
    def set_frame(self, frame):
        self.ui.qlabel_frame.frame = frame
        
    def connect_button_signal(self):
        self.ui.btn_apply.clicked.connect(self.apply)
        self.ui.btn_clear.clicked.connect(self.clear)
        
    def apply(self):
        if self.ui.qlabel_frame.top_left is None or self.ui.qlabel_frame.bottom_right is None:
            x1_scale, y1_scale = 0, 0
            x2_scale, y2_scale = 1, 1
        else:
            x1, y1 = self.ui.qlabel_frame.top_left
            x2, y2 = self.ui.qlabel_frame.bottom_right
            x1_scale, y1_scale = x1 / self.ui.qlabel_frame.width(), y1 / self.ui.qlabel_frame.height()
            x2_scale, y2_scale = x2 / self.ui.qlabel_frame.width(), y2 / self.ui.qlabel_frame.height()
        self.sig_roi.emit((x1_scale, y1_scale, x2_scale, y2_scale))
        self.close()
        
    def clear(self):
        self.ui.qlabel_frame.top_left = None
        self.ui.qlabel_frame.bottom_right = None
        self.ui.qlabel_frame.bottom_right_move = None
        self.ui.qlabel_frame.update()
        
        