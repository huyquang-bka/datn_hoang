from PyQt5 import QtCore
import cv2



class ThreadHeatMap(QtCore.QThread):
    def __init__(self, parent=None, capture_queue=..., output_queue=...):
        super().__init__(parent)
        self.__thread_active = False
        self.capture_queue = capture_queue
        self.output_queue = output_queue
        self.bg_subtractor = cv2.createBackgroundSubtractorMOG2()
        
    def run(self):
        print("ThreadHeatmap: Start")
        self.__thread_active = True
        while self.__thread_active:
            if self.capture_queue.empty():
                self.msleep(1)
                continue
            frame = self.capture_queue.get()
            fg_mask = self.bg_subtractor.apply(frame)
            fg_mask = cv2.medianBlur(fg_mask, 5)            
            fg_mask = cv2.cvtColor(fg_mask, cv2.COLOR_GRAY2BGR)
            if self.output_queue.empty():
                self.output_queue.put(fg_mask)
    
    def stop(self):
        self.__thread_active = False
            
        

        
