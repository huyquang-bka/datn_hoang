from PyQt5 import QtCore
import cv2
import imutils


class ThreadCapture(QtCore.QThread):
    def __init__(self, parent=None, file_name=None, capture_queue=..., capture_queue_heatmap=..., output_queue=...):
        super().__init__(parent)
        self.__thread_active = False
        self.file_name = file_name
        self.capture_queue = capture_queue
        self.output_queue = output_queue
        self.capture_queue_heatmap = capture_queue_heatmap
        
        self.roi = (0, 0, 1, 1)
        
        self.is_inference = False
        
    def get_roi(self, roi):
        self.roi = roi
        
    def get_inference_status(self):
        self.is_inference = False
        
    def scale_to_roi(self, scale_roi, frame_shape):
        x1, y1, x2, y2 = scale_roi
        H, W = frame_shape[:2]
        x1 = int(x1 * W)
        y1 = int(y1 * H)
        x2 = int(x2 * W)
        y2 = int(y2 * H)
        return (x1, y1, x2, y2)
        
    def run(self):
        print("ThreadCapture: Start. File name: {}".format(self.file_name))
        self.__thread_active = True
        cap = cv2.VideoCapture(self.file_name)
        while self.__thread_active:
            ret, frame = cap.read()
            if not ret:
                cap = cv2.VideoCapture(self.file_name)
                continue
            x1, y1, x2, y2 = self.scale_to_roi(self.roi, frame.shape)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            if self.capture_queue_heatmap.empty():
                frame_resize = imutils.resize(frame, width=640)
                self.capture_queue_heatmap.put(frame_resize)
            if self.output_queue.empty():
                self.output_queue.put([frame, [x1, y1, x2, y2]]) 
            if self.capture_queue.empty() and not self.is_inference:
                crop_frame = frame[y1:y2, x1:x2]
                if frame.shape != crop_frame.shape:
                    self.capture_queue.put(crop_frame)
                    self.is_inference = True
            self.msleep(30)
    
    def stop(self):
        self.__thread_active = False
            
        

        
