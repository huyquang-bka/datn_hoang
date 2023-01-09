from ..ui.widget_image import Ui_WidgetImage
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import QtGui
from ...utils.inference_tool import InferenceTool
import cv2


class WidgetImage(QWidget):
    
    def __init__(self, parent=None, inference_tool: InferenceTool = ...):
        super().__init__(parent)
        self.ui = Ui_WidgetImage()
        self.ui.setupUi(self)
        self.inference_tool = inference_tool
        self.image = None
    
    def start(self, file_name):
        image = cv2.imread(file_name)
        self.image = image.copy()
        self.ui.qlabel_num_of_person.setText("Inference...")
        rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # self.show_image(rgb_img)
        num_person = self.inference_tool.predict(rgb_img)
        num_person = round(num_person)
        self.ui.qlabel_num_of_person.setText(str(num_person))
    
    def stop(self):
        self.ui.qlabel_frame.clear()
        self.ui.qlabel_num_of_person.setText("0")

    def paintEvent(self, event):
        if self.image is not None:
            rgb_img = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            self.show_image(rgb_img)
        self.update()

    def show_image(self, rgb_img):
        rgb_img = cv2.resize(rgb_img, (self.ui.qlabel_frame.width(), self.ui.qlabel_frame.height()))
        qt_img = QtGui.QPixmap.fromImage(
            QtGui.QImage(rgb_img.data, rgb_img.shape[1], rgb_img.shape[0], QtGui.QImage.Format_RGB888)).scaled(
            self.ui.qlabel_frame.width(), self.ui.qlabel_frame.height())
        self.ui.qlabel_frame.setPixmap(qt_img)
        self.ui.qlabel_frame.setScaledContents(True)
            
        