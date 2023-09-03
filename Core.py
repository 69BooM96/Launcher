import subprocess
import sys
import os
import easygui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileSystemModel
from PyQt5 import QtCore, QtGui, QtWidgets

import launcher


class ExampleApp(QtWidgets.QMainWindow, launcher.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.settings)
        self.pushButton_3.clicked.connect(self.open_folder)

    def settings(self):
        #Start
        print("Start")

    def open_folder(self):
        directory = r".."
        input_file = easygui.diropenbox(default=directory)
        print(input_file)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()