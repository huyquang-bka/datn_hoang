from PyQt5 import QtCore
import cv2
from ..utils.inference_tool import predict


class ThreadInference(QtCore.QThread):
    sig_num_person = QtCore.pyqtSignal(str)
    
    def __init__(self, parent=None, capture_queue=...):
        super().__init__(parent)
        self.__thread_active = False
        self.capture_queue = capture_queue
    
    def run(self):
        print("ThreadInference: Start")
        self.__thread_active = True
        while self.__thread_active:
            if self.capture_queue.empty():
                self.msleep(1)
                continue
            frame = self.capture_queue.get()
            num_person = predict(frame)
            num_person = round(num_person)
            self.sig_num_person.emit(str(num_person))
    
    def stop(self):
        self.__thread_active = False
            
        

        
