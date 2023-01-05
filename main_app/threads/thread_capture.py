from PyQt5 import QtCore
import cv2


class ThreadCapture(QtCore.QThread):
    def __init__(self, parent=None, file_name=None, capture_queue=..., output_queue=...):
        super().__init__(parent)
        self.__thread_active = False
        self.file_name = file_name
        self.capture_queue = capture_queue
        self.output_queue = output_queue
    
    def run(self):
        print("ThreadCapture: Start. File name: {}".format(self.file_name))
        self.__thread_active = True
        cap = cv2.VideoCapture(self.file_name)
        while self.__thread_active:
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            if self.capture_queue.empty():
                self.capture_queue.put(frame)
            if self.output_queue.empty():
               self.output_queue.put(frame) 
            self.msleep(30)
    
    def stop(self):
        self.__thread_active = False
            
        

        
