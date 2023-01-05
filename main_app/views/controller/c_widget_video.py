import cv2
from ..ui.widget_video import Ui_WidgetVideo
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import QtGui, QtCore
from ...threads.thread_capture import ThreadCapture
from ...threads.thread_inference import ThreadInference
from queue import Queue


class WidgetVideo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_WidgetVideo()
        self.ui.setupUi(self)
        
        self.ui.qlabel_frame.setScaledContents(True)
        
        self.define_queue()
    
    def define_queue(self):
        self.capture_queue = Queue()
        self.output_queue = Queue()
        
    def start(self, file_name, limit_person):
        self.list_thread = []
        self.capture_queue = Queue()
        self.output_queue = Queue()
        
        self.thread_capture = ThreadCapture(file_name=file_name, capture_queue=self.capture_queue, output_queue=self.output_queue)
        self.thread_inference = ThreadInference(capture_queue=self.capture_queue)
        
        self.list_thread.append(self.thread_capture)
        self.list_thread.append(self.thread_inference)
        
        self.connect_signal()
        self.start_all_thread()
    
    def connect_signal(self):
        self.thread_inference.sig_num_person.connect(self.get_num_person)
        
    def get_num_person(self, str):
        self.ui.qlabel_num_of_person.setText(str)
        
    def start_all_thread(self):
        for thread in self.list_thread:
            thread.start()
    
    def stop(self):
        for thread in self.list_thread:
            thread.stop()
            
    def paintEvent(self, e) -> None:
        if self.output_queue.empty():
            QtCore.QThread.msleep(1)
            return
        frame = self.output_queue.get()
        self.show_image(frame)
    
    def show_image(self, rgb_img):
        rgb_img = cv2.resize(rgb_img, (self.ui.qlabel_frame.width(), self.ui.qlabel_frame.height()))
        qt_img = QtGui.QPixmap.fromImage(
            QtGui.QImage(rgb_img.data, rgb_img.shape[1], rgb_img.shape[0], QtGui.QImage.Format_RGB888)).scaled(
            self.ui.qlabel_frame.width(), self.ui.qlabel_frame.height())
        self.ui.qlabel_frame.setPixmap(qt_img)
    
    
    