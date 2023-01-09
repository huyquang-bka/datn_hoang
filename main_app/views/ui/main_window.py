# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources\ui\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1051, 843)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox.setStyleSheet("background-color: rgb(173, 221, 230);\n"
"border: 2px solid black;\n"
"border-radius: 6px;\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.combo_options = QtWidgets.QComboBox(self.groupBox)
        self.combo_options.setGeometry(QtCore.QRect(9, 40, 91, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_options.sizePolicy().hasHeightForWidth())
        self.combo_options.setSizePolicy(sizePolicy)
        self.combo_options.setMinimumSize(QtCore.QSize(0, 0))
        self.combo_options.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 6px;")
        self.combo_options.setObjectName("combo_options")
        self.combo_options.addItem("")
        self.combo_options.addItem("")
        self.btn_choose_file = QtWidgets.QPushButton(self.groupBox)
        self.btn_choose_file.setGeometry(QtCore.QRect(110, 40, 81, 26))
        self.btn_choose_file.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_choose_file.setStyleSheet("QPushButton {\n"
"            background-color: rgb(255, 255, 255); \n"
"        }\n"
"QPushButton:pressed {\n"
"            background-color: rgb(127, 127, 127);\n"
"        }")
        self.btn_choose_file.setObjectName("btn_choose_file")
        self.btn_start = QtWidgets.QPushButton(self.groupBox)
        self.btn_start.setGeometry(QtCore.QRect(11, 150, 80, 26))
        self.btn_start.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_start.setStyleSheet("QPushButton {\n"
"            background-color: rgb(255, 255, 255); \n"
"        }\n"
"QPushButton:pressed {\n"
"            background-color: rgb(127, 127, 127);\n"
"        }")
        self.btn_start.setObjectName("btn_start")
        self.btn_stop = QtWidgets.QPushButton(self.groupBox)
        self.btn_stop.setGeometry(QtCore.QRect(111, 150, 80, 26))
        self.btn_stop.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_stop.setStyleSheet("QPushButton {\n"
"            background-color: rgb(255, 255, 255); \n"
"        }\n"
"QPushButton:pressed {\n"
"            background-color: rgb(127, 127, 127);\n"
"        }")
        self.btn_stop.setObjectName("btn_stop")
        self.qtext_file_path = QtWidgets.QTextEdit(self.groupBox)
        self.qtext_file_path.setGeometry(QtCore.QRect(10, 80, 181, 51))
        self.qtext_file_path.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 6px;")
        self.qtext_file_path.setObjectName("qtext_file_path")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 2, 1)
        self.qframe_widget = QtWidgets.QFrame(self.centralwidget)
        self.qframe_widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 6px;")
        self.qframe_widget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.qframe_widget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.qframe_widget.setObjectName("qframe_widget")
        self.gridLayout.addWidget(self.qframe_widget, 0, 1, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1051, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.combo_options.setItemText(0, _translate("MainWindow", "Image"))
        self.combo_options.setItemText(1, _translate("MainWindow", "Video"))
        self.btn_choose_file.setText(_translate("MainWindow", "Choose File"))
        self.btn_start.setText(_translate("MainWindow", "Start"))
        self.btn_stop.setText(_translate("MainWindow", "Stop"))
        self.qtext_file_path.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:13pt;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
