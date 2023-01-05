from ..ui.main_window import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QGridLayout, QVBoxLayout, QMessageBox
from .c_widget_image import WidgetImage
from .c_widget_video import WidgetVideo


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #define variables
        self.define_variables()
        
        #connect btn signals
        self.connect_btn_signals()
        
    def define_variables(self):
        self.file_name = ""
        
        self.widget_image = WidgetImage()
        self.widget_video = WidgetVideo()
        
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
        if not self.file_name or self.file_name is None:
            QMessageBox.about(self, "Error", "Please choose a file")
            return
        limit_person = self.ui.qline_limit_person.text()
        if self.current_option_index == 0:
            self.widget_image.start(self.file_name, limit_person)
        elif self.current_option_index == 1:
            self.widget_video.start(self.file_name, limit_person)
    
    def stop(self):
        if self.current_option_index == 0:
            self.widget_image.stop()
        elif self.current_option_index == 1:
            self.widget_video.stop()
            