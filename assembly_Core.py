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
import assembly
import minecraft_launcher_lib

class ExampleApp(QtWidgets.QMainWindow, assembly.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.update_mod_list()
        self.update_shader_list()
        self.update_texture_list()
        self.icons()
        self.version()
        self.pushButton.clicked.connect(self.create_assembly)
        self.pushButton_2.clicked.connect(self.cancellation)
        self.listWidget_5.clicked.connect(self.mod_assembly_on)
        self.listWidget_6.clicked.connect(self.mod_assembly_off)
        self.listWidget_3.clicked.connect(self.texture_assembly_on)
        self.listWidget_4.clicked.connect(self.texture_assembly_off)
        self.listWidget.clicked.connect(self.shader_assembly_on)
        self.listWidget_2.clicked.connect(self.shader_assembly_off)


    def version(self):
        for version in minecraft_launcher_lib.utils.get_installed_versions(minecraft_directory=".minecraft"):
            icon3 = QtGui.QIcon()
            icon3.addPixmap(QtGui.QPixmap(f"res/version2.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            self.comboBox_2.addItem(icon3, version["id"])

    def icons(self):
        update = os.listdir("res/icon/")
        for icon_list in update:
            icon3 = QtGui.QIcon()
            icon3.addPixmap(QtGui.QPixmap(f"res/icon/{icon_list}"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            update2 = icon_list.replace(".png", "")
            self.comboBox_3.addItem(icon3, f"{update2}")

    def mod_assembly_on(self):
        item = self.listWidget_5.currentItem()
        print(item.text())
        for item2 in self.listWidget_5.selectedIndexes():
            print(item2.row())
            self.listWidget_5.takeItem(item2.row())
            self.listWidget_6.addItem(item.text())

    def mod_assembly_off(self):
        item = self.listWidget_6.currentItem()
        print(item.text())
        for item2 in self.listWidget_6.selectedIndexes():
            print(item2.row())
            self.listWidget_6.takeItem(item2.row())
            self.listWidget_5.addItem(item.text())

    def texture_assembly_on(self):
        item = self.listWidget_3.currentItem()
        print(item.text())
        for item2 in self.listWidget_3.selectedIndexes():
            print(item2.row())
            self.listWidget_3.takeItem(item2.row())
            self.listWidget_4.addItem(item.text())

    def texture_assembly_off(self):
        item = self.listWidget_4.currentItem()
        print(item.text())
        for item2 in self.listWidget_4.selectedIndexes():
            print(item2.row())
            self.listWidget_4.takeItem(item2.row())
            self.listWidget_3.addItem(item.text())

    def shader_assembly_on(self):
        item = self.listWidget.currentItem()
        print(item.text())
        for item2 in self.listWidget.selectedIndexes():
            print(item2.row())
            self.listWidget.takeItem(item2.row())
            self.listWidget_2.addItem(item.text())

    def shader_assembly_off(self):
        item = self.listWidget_2.currentItem()
        print(item.text())
        for item2 in self.listWidget_2.selectedIndexes():
            print(item2.row())
            self.listWidget_2.takeItem(item2.row())
            self.listWidget.addItem(item.text())

    def update_mod_list(self):
        self.listWidget_5.clear()
        update = os.listdir("minecraft/mods")
        for mod_list in update:
            self.listWidget_5.addItem(mod_list)

    def update_texture_list(self):
        self.listWidget_3.clear()
        update = os.listdir("minecraft/textures")
        for texture_list in update:
            self.listWidget_3.addItem(texture_list)

    def update_shader_list(self):
        self.listWidget.clear()
        update = os.listdir("minecraft/shaders")
        for shader_list in update:
            self.listWidget.addItem(shader_list)

    def create_assembly(self):
        print("creat")
        name = self.lineEdit.text()
        version = self.comboBox_2.currentText()
        icon = self.comboBox_3.currentIndex()

        file = open(f'minecraft/assembly/{name}.assembly', mode='w', encoding='utf-8')
        file.write("name:" + f"{name}\n")
        file.write("version:" + f"{version}\n")
        file.write("icon:" + f"{icon}\n")
        file.write("mods:[\n")
        for i in range(self.listWidget_6.count()):
            item = self.listWidget_6.item(i)
            print(item.text())
            file.write(item.text() + "\n")
        file.write("]\n")
        file.write("textures:[\n")
        for i in range(self.listWidget_4.count()):
            item = self.listWidget_4.item(i)
            print(item.text())
            file.write(item.text() + "\n")
        file.write("]\n")
        file.write("shaders:[\n")
        for i in range(self.listWidget_2.count()):
            item = self.listWidget_2.item(i)
            print(item.text())
            file.write(item.text() + "\n")
        file.write("]")
        file.close()
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