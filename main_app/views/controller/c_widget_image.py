from ..ui.widget_image import Ui_WidgetImage
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt5 import QtGui
from ...utils.inference_tool import predict
import cv2


class WidgetImage(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_WidgetImage()
        self.ui.setupUi(self)
    
    def start(self, file_name, limit_person):
        image = cv2.imread(file_name)
        rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.show_image(rgb_img)
        num_person = predict(rgb_img)
        num_person = round(num_person)
        self.ui.qlabel_num_of_person.setText(str(num_person))
        try:
            limit_person = float(limit_person)
        except:
            limit_person = -1
        if limit_person > 0 and num_person > limit_person:
            QMessageBox.warning(self, "Warning", "Number of people is greater than limit people")
    
    def stop(self):
        self.ui.qlabel_frame.clear()
        self.ui.qlabel_num_of_person.setText("0")

    def show_image(self, rgb_img):
        rgb_img = cv2.resize(rgb_img, (self.ui.qlabel_frame.width(), self.ui.qlabel_frame.height()))
        qt_img = QtGui.QPixmap.fromImage(
            QtGui.QImage(rgb_img.data, rgb_img.shape[1], rgb_img.shape[0], QtGui.QImage.Format_RGB888)).scaled(
            self.ui.qlabel_frame.width(), self.ui.qlabel_frame.height())
        self.ui.qlabel_frame.setPixmap(qt_img)
        self.ui.qlabel_frame.setScaledContents(True)
            
        