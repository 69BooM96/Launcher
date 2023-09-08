import subprocess
import sys
from pathlib import Path
import easygui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileSystemModel
from PyQt5 import QtCore, QtGui, QtWidgets
import zipfile
import os
import shutil

import launcher

class ExampleApp(QtWidgets.QMainWindow, launcher.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.settings)
        self.pushButton_3.clicked.connect(self.open_folder)
        self.radioButton.clicked.connect(self.white)
        self.radioButton_2.clicked.connect(self.dark)
        self.pushButton_7.clicked.connect(self.texture)
        self.pushButton_8.clicked.connect(self.shaders)
        self.pushButton_6.clicked.connect(self.mods)
        self.pushButton_19.clicked.connect(self.open_jar)
        self.pushButton_18.clicked.connect(self.delete_jar)

    def shaders(self):
        self.label_6.setText("Шейдеры")

    def texture(self):
        self.label_6.setText("Текстуры")

    def mods(self):
        self.label_6.setText("Моды")

    def open_jar(self):
        input_file = easygui.fileopenbox(title='Import file',default='*',filetypes=["*.jar", "*.zip"])
        file_path = Path(input_file)
        Mod = False
        Texture = False
        file_open = zipfile.ZipFile(input_file, "r")
        for file_copy in file_open.infolist():
            if file_copy.filename == "mcmod.info":
                Mod = True

            if file_copy.filename == "pack.mcmeta":
                Texture = True


        if Mod == False:
            if Texture == True:
                print("Texture")

            if Texture == False:
                print("Shaders")

        if Mod == True:
            print("Mod")
            os.mkdir("./minecraft/imports")
            file_open.extractall("./minecraft/imports")
            file_zip = zipfile.ZipFile(file_path, "w")
            for folder, subfolders, files in os.walk("./minecraft/imports"):
                for file in files:
                    file_zip.write(os.path.join(folder, file),
                                   os.path.relpath(os.path.join(folder, file), "/minecraft/mods"),
                                   compress_type=zipfile.ZIP_DEFLATED)
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), './minecraft/imports')
            shutil.rmtree(path)

        file_open.close()

    def delete_jar(self):
        print("del")

    def dark(self):
        self.frame_2.setStyleSheet("background-color: rgba(49, 49, 49);")
        self.pushButton.setStyleSheet("color: rgb(240, 255, 255);\n"
                                      "background-color: rgba(0, 0, 0, 0);")
        self.pushButton_3.setStyleSheet("color: rgb(240, 255, 255);\n"
                                        "background-color: rgba(0, 0, 0, 0);")
        self.pushButton_13.setStyleSheet("color: rgb(240, 255, 255);\n"
                                         "background-color: rgba(0, 0, 0, 0);")
        self.pushButton_14.setStyleSheet("color: rgb(240, 255, 255);\n"
                                         "background-color: rgba(0, 0, 0, 0);")
        self.pushButton_12.setStyleSheet("color: rgb(240, 255, 255);\n"
                                         "background-color: rgba(0, 0, 0, 0);")
        self.pushButton_2.setStyleSheet("color: rgb(240, 255, 255);\n"
                                         "background-color: rgba(0, 0, 0, 0);")
        self.pushButton_15.setStyleSheet("border: 12px solid rgba(49, 49, 49);"
                                         "background-color: rgba(255, 255, 255, 0);"
                                         "border-radius: 30px;")
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color: rgb(39, 39, 39);")
        self.tabWidget.setStyleSheet("QTabBar {\n"
                                     "    background-color: rgb(39, 39, 39);     \n"
                                     "}\n"
                                     "QTabBar::tab {\n"
                                     "    background-color: rgb(39, 39, 39);\n"
                                     "    color: rgb(200, 187, 179);\n"
                                     "}\n"
                                     "QTabBar::tab:selected {\n"
                                     "    background-color: rgb(39, 39, 39);\n"
                                     "    color: rgb(249, 249, 249);\n"
                                     "    background-color: qlineargradient(spread:pad, x1:0, y1:1, stop:0.01 rgb(30, 147, 10), stop:0.15 rgba(255, 255, 255, 0));\n"
                                     "}")
        self.comboBox.setStyleSheet("QComboBox {\n"
                                    "    border-radius: 3px;\n"
                                    "    padding: 1px 18px 1px 3px;\n"
                                    "    min-width: 6em;\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox:!editable, QComboBox::drop-down:editable {\n"
                                    "    background-color: rgba(0, 0, 0, 0);\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox::drop-down {\n"
                                    "    subcontrol-origin: padding;\n"
                                    "    subcontrol-position: top right;\n"
                                    "    width: 15px;\n"
                                    "    border-left-color: darkgray;\n"
                                    "    border-left-style: solid;\n"
                                    "    border-top-right-radius: 3px;\n"
                                    "    border-bottom-right-radius: 3px;\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox::down-arrow {\n"
                                    "    image: url(C:/Users/студент.BestLaptop-ПК/Desktop/лаунчер/res/open.png);\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox::down-arrow:on {\n"
                                    "    top: 0px;\n"
                                    "    left: 0px;\n"
                                    "}")
        self.frame_7.setStyleSheet("border: 3px solid rgba(69, 69, 69);\n"
                                   "background-color: rgba(255, 255, 255, 0);\n"
                                   "border-radius: 17px;")
        self.tab_5.setStyleSheet("background-color: rgba(52, 52, 52);\n"
                                 "color: rgb(240, 255, 255);")
        self.tab_6.setStyleSheet("background-color: rgba(52, 52, 52);\n"
                                 "color: rgb(240, 255, 255);")

    def white(self):
        self.frame_2.setStyleSheet("background-color: rgba(235, 235, 235);")
        self.pushButton.setStyleSheet("color: rgb(4, 5, 5);\n"
                                      "background-color: rgba(0, 0, 0, 0);")
        self.pushButton_3.setStyleSheet("color: rgb(4, 5, 5);\n"
                                        "background-color: rgba(0, 0, 0, 0);")
        self.pushButton_13.setStyleSheet("color: rgb(4, 5, 5);\n"
                                         "background-color: rgba(0, 0, 0, 0);")
        self.pushButton_14.setStyleSheet("color: rgb(4, 5, 5);\n"
                                         "background-color: rgba(0, 0, 0, 0);")
        self.pushButton_12.setStyleSheet("color: rgb(4, 5, 5);\n"
                                         "background-color: rgba(0, 0, 0, 0);")
        self.pushButton_2.setStyleSheet("color: rgb(4, 5, 5);\n"
                                        "background-color: rgba(0, 0, 0, 0);")
        self.pushButton_15.setStyleSheet("border: 12px solid rgba(235, 235, 235);"
                                         "background-color: rgba(255, 255, 255, 0);"
                                         "border-radius: 30px;")
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "background-color: rgb(215, 215, 215);")
        self.comboBox.setStyleSheet("QComboBox {\n"
                                    "    border-radius: 3px;\n"
                                    "    padding: 1px 18px 1px 3px;\n"
                                    "    min-width: 6em;\n"
                                    "    color: rgb(0, 0, 0);\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox:!editable, QComboBox::drop-down:editable {\n"
                                    "    background-color: rgba(0, 0, 0, 0);\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox::drop-down {\n"
                                    "    subcontrol-origin: padding;\n"
                                    "    subcontrol-position: top right;\n"
                                    "    width: 15px;\n"
                                    "    border-left-color: darkgray;\n"
                                    "    border-left-style: solid;\n"
                                    "    border-top-right-radius: 3px;\n"
                                    "    border-bottom-right-radius: 3px;\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox::down-arrow {\n"
                                    "    image: url(C:/Users/студент.BestLaptop-ПК/Desktop/лаунчер/res/open_black.png);\n"
                                    "}\n"
                                    "\n"
                                    "QComboBox::down-arrow:on {\n"
                                    "    top: 0px;\n"
                                    "    left: 0px;\n"
                                    "}")
        self.tabWidget.setStyleSheet("QTabBar {\n"
                                     "    background-color: rgb(215, 215, 215);     \n"
                                     "}\n"
                                     "QTabBar::tab {\n"
                                     "    background-color: rgb(215, 215, 215);\n"
                                     "    color: rgb(80, 80, 80);\n"
                                     "}\n"
                                     "QTabBar::tab:selected {\n"
                                     "    background-color: rgb(215, 215, 215);\n"
                                     "    color: rgb(9, 9, 9);\n"
                                     "    background-color: qlineargradient(spread:pad, x1:0, y1:1, stop:0.01 rgb(30, 147, 10), stop:0.15 rgba(255, 255, 255, 0));\n"
                                     "}")
        self.frame_7.setStyleSheet("border: 3px solid rgba(180, 180, 180);\n"
                                   "background-color: rgba(255, 255, 255, 0);\n"
                                   "border-radius: 17px;")
        self.tab_5.setStyleSheet("background-color: rgba(232, 232, 232);\n"
                                 "color: rgb(0, 0, 0);")
        self.tab_6.setStyleSheet("background-color: rgba(232, 232, 232);\n"
                                 "color: rgb(0, 0, 0);")


    def settings(self):
        #Start
        print("x")

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