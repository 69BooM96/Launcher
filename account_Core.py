import subprocess
import sys
from pathlib import Path
import easygui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileSystemModel, QListWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
import zipfile
import os
import shutil
import account

class ExampleApp(QtWidgets.QMainWindow, account.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.create_assembly)
        self.pushButton_2.clicked.connect(self.cancellation)


    def create_assembly(self):
        name = self.lineEdit.text()
        file = open('user.info', mode='a', encoding='utf-8')
        file.write(name + "\n")
        quit()

    def cancellation(self):
        quit()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()