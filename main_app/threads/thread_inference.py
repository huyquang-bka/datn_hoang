from PyQt5 import QtCore
import cv2


class ThreadInference(QtCore.QThread):
    sig_num_person = QtCore.pyqtSignal(str)
    sig_is_inference = QtCore.pyqtSignal()
    
    def __init__(self, parent=None, capture_queue=..., inference_tool=...):
        super().__init__(parent)
        self.__thread_active = False
        self.capture_queue = capture_queue
        self.inference_tool = inference_tool
        self.frame = None
    
    def run(self):
        print("ThreadInference: Start")
        self.__thread_active = True
        while self.__thread_active:
            if self.capture_queue.empty():
                self.msleep(1)
                continue
            frame = self.capture_queue.get()
            self.frame = frame
            num_person = self.inference_tool.predict(frame)
            num_person = round(num_person)
            self.sig_num_person.emit(str(num_person))
            self.sig_is_inference.emit()
    
    def stop(self):
        self.__thread_active = False
            
        

        
