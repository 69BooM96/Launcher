import subprocess
import sys
from minecraft_launcher_lib import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileSystemModel, QListWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
import os

from minecraft_launcher_lib.command import get_minecraft_command
from minecraft_launcher_lib.install import install_minecraft_version
import settings
from uuid import uuid1
import time

class ExampleApp(QtWidgets.QMainWindow, settings.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_7.clicked.connect(self.save)
        self.pushButton_11.clicked.connect(self.colors)
        self.pushButton_12.clicked.connect(self.memory)
        self.memory()

    def colors(self):
        color_r = self.horizontalSlider_2.value()
        color_g = self.horizontalSlider_3.value()
        color_a = self.horizontalSlider_4.value()
        color_b = self.horizontalSlider_5.value()
        self.label_13.setStyleSheet(f"background-color: rgba({color_r}, {color_g}, {color_b}, {color_a});")

    def memory(self):
        memory_allocation = self.horizontalSlider_6.value()
        print(memory_allocation)
        self.spinBox_6.setProperty("value", memory_allocation)

    def save(self):
        language = self.comboBox.currentText()
        auto_backups = self.checkBox_3.isChecked()
        baground = self.lineEdit.text()
        bagrounds = self.checkBox.isChecked()
        color_r = self.horizontalSlider_2.value()
        color_g = self.horizontalSlider_3.value()
        color_b = self.horizontalSlider_4.value()
        color_a = self.horizontalSlider_5.value()
        auto_update = self.checkBox_2.isChecked()
        path_backups = self.lineEdit_2.text()
        close_l = self.checkBox_4.isChecked()
        close_d = self.checkBox_5.isChecked()
        #Start MineCraft
        director = self.lineEdit_3.text()
        permission_1 = self.spinBox_4.text()
        permission_2 = self.spinBox_5.text()
        full_screen_mode = self.checkBox_6.isChecked()
        arg_1 = self.lineEdit_4.text()
        arg_2 = self.lineEdit_5.text()
        Java_selection = self.lineEdit_6.text()
        memory_allocation = self.horizontalSlider_6.value()
        file = open("settings.stg", "w")
        file.write(f'language={language}\nauto_backups={auto_backups}\nbaground={baground}\nbagrounds={bagrounds}\ncolor_r={color_r}\ncolor_g={color_g}\ncolor_b={color_b}\ncolor_a={color_a}\nauto_update={auto_update}\npath_backups={path_backups}\nclose_l={close_l}\nclose_d={close_d}\ndirector={director}\npermission_1={permission_1}\npermission_2={permission_2}\nfull_screen_mode={full_screen_mode}\narg_1={arg_1}\narg_2={arg_2}\nJava_selection={Java_selection}\nassembly=false\n')
        file.close()
        file = open("javaArg.info", "w")
        file.write(f'{memory_allocation}')
        file.close()



        #Settings MineCraft

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()