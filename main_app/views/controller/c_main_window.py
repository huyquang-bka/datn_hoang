import time
from ..ui.main_window import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QGridLayout, QMessageBox
from .c_widget_image import WidgetImage
from .c_widget_video import WidgetVideo
from ...utils.inference_tool import InferenceTool


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Crowd Counting App")
        
        #define variables
        self.define_variables()
        
        #connect btn signals
        self.connect_btn_signals()
                        
    def define_variables(self):
        self.file_name = ""
        self.inference_tool = InferenceTool()
        
        self.widget_image = WidgetImage(inference_tool=self.inference_tool)
        self.widget_video = WidgetVideo(inference_tool=self.inference_tool)
        
        self.grid_layout_cameras = QGridLayout()
        self.grid_layout_cameras.setContentsMargins(0, 0, 0, 0)
        self.ui.qframe_widget.setLayout(self.grid_layout_cameras)
        self.grid_layout_cameras.addWidget(self.widget_image, 0, 0)
        self.grid_layout_cameras.addWidget(self.widget_video, 0, 0)
        self.widget_video.hide()
        
        self.current_widget = self.widget_image
        
        self.current_option_index = self.ui.combo_options.currentIndex() 
        
    def connect_btn_signals(self):
        self.ui.btn_choose_file.clicked.connect(self.choose_file)
        self.ui.combo_options.currentIndexChanged.connect(self.change_option)
        self.ui.btn_start.clicked.connect(self.start)
        self.ui.btn_stop.clicked.connect(self.stop)
        
    def choose_file(self):
        if self.current_option_index == 0:
            file_name, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Image Files (*.png *.jpg *.jpeg)')
        elif self.current_option_index == 1:
            file_name, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Video Files (*.mp4 *.mov *.avi)')
        self.file_name = file_name
        self.ui.qtext_file_path.setText(self.file_name)

    def change_option(self):
        print("change_option: ", self.ui.combo_options.currentIndex())
        self.current_option_index = self.ui.combo_options.currentIndex()
        if self.current_option_index == 0:
            self.file_name = ""
            self.widget_image.show()
            self.widget_video.hide()
        elif self.current_option_index == 1:
            self.file_name = ""
            self.widget_image.hide()
            self.widget_video.show()

    def start(self):
        fn = self.ui.qtext_file_path.toPlainText()
        if not fn:
            QMessageBox.about(self, "Error", "Please choose a file")
            return
        if self.current_option_index == 0:
            self.widget_image.start(fn)
        elif self.current_option_index == 1:
            self.widget_video.start(fn)
            self.ui.btn_start.setEnabled(False)
            self.ui.btn_stop.setEnabled(True)
    
    def stop(self):
        if self.current_option_index == 0:
            self.widget_image.stop()
        elif self.current_option_index == 1:
            self.widget_video.stop()
            self.ui.btn_start.setEnabled(True)
            self.ui.btn_stop.setEnabled(False)
            