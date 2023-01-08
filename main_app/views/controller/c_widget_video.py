import time
import cv2
from ..ui.widget_video import Ui_WidgetVideo
from .c_widget_draw import WidgetDraw
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import QtGui, QtCore
from ...threads.thread_capture import ThreadCapture
from ...threads.thread_inference import ThreadInference
from ...threads.thread_heatmap import ThreadHeatMap
from queue import Queue


class WidgetVideo(QWidget):
    def __init__(self, parent=None, inference_tool=...):
        super().__init__(parent)
        self.ui = Ui_WidgetVideo()
        self.ui.setupUi(self)
        
        self.widget_draw = WidgetDraw()
        
        self.frame = None
        
        self.connect_button_signal()
        
        self.ui.qlabel_frame.setScaledContents(True)
        
        self.define_queue()
        self.inference_tool = inference_tool
        
        self.ui.qlabel_warning.hide()
        
        self.list_thread = []
        
        self.color = (0, 255, 0) 
    
    def define_queue(self):
        self.capture_queue = Queue()
        self.capture_queue_heatmap = Queue()
        self.output_queue = Queue()
        self.output_queue_heatmap = Queue()
        
    def start(self, file_name):
        self.ui.qlabel_crop_frame.clear()
        self.ui.qlabel_warning.hide()
        self.ui.qlabel_num_of_person.setText("People estimate: 0")
        
        self.thread_capture = ThreadCapture(file_name=file_name, capture_queue=self.capture_queue, capture_queue_heatmap=self.capture_queue_heatmap, output_queue=self.output_queue)
        self.thread_inference = ThreadInference(capture_queue=self.capture_queue, inference_tool=self.inference_tool)
        self.thread_heatmap = ThreadHeatMap(capture_queue=self.capture_queue_heatmap, output_queue=self.output_queue_heatmap)
        
        self.list_thread.append(self.thread_capture)
        self.list_thread.append(self.thread_inference)
        self.list_thread.append(self.thread_heatmap)
        
        self.connect_signal()
        self.start_all_thread()
    
    def connect_button_signal(self):
        self.ui.btn_draw_roi.clicked.connect(self.draw_roi)
        
    def draw_roi(self):
        if self.frame is None:
            QMessageBox.warning(self, "Warning", "Please start video first")
            return
        self.widget_draw.set_frame(self.frame)
        self.widget_draw.show()
    
    def connect_signal(self):
        self.thread_inference.sig_num_person.connect(self.get_num_person)
        self.widget_draw.sig_roi.connect(self.thread_capture.get_roi)
        self.thread_inference.sig_is_inference.connect(self.thread_capture.get_inference_status)
        # pass
        
    def get_num_person(self, num_person):
        text = "People estimate: " + str(num_person)
        self.ui.qlabel_num_of_person.setText(text)
        if self.thread_inference.frame is not None:
            frame = self.thread_inference.frame.copy()
            frame = cv2.resize(frame, (640, 480))
            self.show_image(frame, self.ui.qlabel_crop_frame)
        limit_person = self.ui.qline_limit.text()
        try:
            limit_person = float(limit_person)
        except:
            limit_person = -1
        if limit_person >= 0 and float(num_person) >= limit_person:
            self.color = (255, 0, 0)
            self.ui.qlabel_warning.show()
        else:
            self.color = (0, 255, 0)
            self.ui.qlabel_warning.hide()
        
    def start_all_thread(self):
        for thread in self.list_thread:
            thread.start()
    
    def stop(self):
        for thread in self.list_thread:
            thread.stop()
        self.list_thread.clear()
            
    def paintEvent(self, e) -> None:
        if not self.output_queue.empty():
            frame, bbox = self.output_queue.get()
            self.frame = frame
            x1, y1, x2, y2 = bbox
            frame_copy = frame.copy()
            cv2.rectangle(frame_copy, (x1, y1), (x2, y2), self.color, 4)
            self.show_image(frame_copy, self.ui.qlabel_frame)
        if not self.output_queue_heatmap.empty():
            frame_heatmap = self.output_queue_heatmap.get()
            self.show_image(frame_heatmap, self.ui.qlabel_heatmap)
        self.update()
    
    def show_image(self, rgb_img, qlabel_frame):
        # rgb_img = cv2.resize(rgb_img, (qlabel_frame.width(), qlabel_frame.height()))
        qt_img = QtGui.QPixmap.fromImage(
            QtGui.QImage(rgb_img.data, rgb_img.shape[1], rgb_img.shape[0], QtGui.QImage.Format_RGB888)).scaled(
            qlabel_frame.width(), qlabel_frame.height())
        qlabel_frame.setPixmap(qt_img)
    
    
    