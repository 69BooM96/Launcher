import subprocess
import sys
from minecraft_launcher_lib import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileSystemModel, QListWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import zipfile
from minecraft_launcher_lib.command import get_minecraft_command
from minecraft_launcher_lib.install import install_minecraft_version
import Download
from uuid import uuid1
import time
import shutil
from pathlib import Path

minecraft_directory = '.minecraft'

class Launcher(QtCore.QThread):
    progress_update_signal = QtCore.pyqtSignal(int, int, str)
    state_update_signal = QtCore.pyqtSignal(bool)

    progress = 0
    progress_max = 0
    progress_label = ''

    def __init__(self):
        super().__init__()

    def update_progress_label(self, value):
        self.progress_label = value
        self.progress_update_signal.emit(self.progress, self.progress_max, self.progress_label)

    def update_progress(self, value):
        self.progress = value
        self.progress_update_signal.emit(self.progress, self.progress_max, self.progress_label)

    def update_progress_max(self, value):
        self.progress_max = value
        self.progress_update_signal.emit(self.progress, self.progress_max, self.progress_label)


    def run(self):
        file = open("version.info", mode="r")
        f2 = file.read()
        file.close()
        file2 = open("username.info", mode="r")
        f1 = file2.read()
        file2.close()
        file2 = open("javaArg.info", mode="r")
        f3 = file2.read()
        file2.close()

        self.state_update_signal.emit(True)


        install_minecraft_version(versionid=f2, minecraft_directory=minecraft_directory, callback={'setStatus': self.update_progress_label, 'setProgress': self.update_progress, 'setMax': self.update_progress_max})
        options = {
            'username': f1,
            'uuid': str(uuid1()),
            'token': '',
            'demo': False,
            'jvmArguments': [f"-Xmx{f3}M", f"-Xms{f3}M"]
        }
        subprocess.call(get_minecraft_command(version=f2, minecraft_directory=minecraft_directory, options=options))
        self.state_update_signal.emit(False)


class ExampleApp(QtWidgets.QMainWindow, Download.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        path = 'res/GIF/BKfh.gif'
        gif = QtGui.QMovie(path)  # !!!
        self.label_4.setMovie(gif)
        gif.start()

        self.Launch = Launcher()

        self.Launch.state_update_signal.connect(self.state_update)
        self.Launch.progress_update_signal.connect(self.update_progress)
        self.launch_game()

    def state_update(self, value):
        self.label.setVisible(value)
        self.progressBar.setVisible(value)
    def update_progress(self, progress, max_progress, label):
        self.progressBar.setValue(progress)
        self.progressBar.setMaximum(max_progress)
        self.label.setText(label)

    def launch_game(self):

        file = open("settings.stg", "r")
        for files in file:
            if files == "assembly=false\n":
                print('false')
                self.Launch.start()
            elif files == "assembly=true\n":
                print('true')
                global assembly_m
                file2 = open("version.info", "r")
                assembly_m = file2.read()
                assembly_m = "minecraft/assembly/" + assembly_m

                path = os.path.join(os.path.abspath(os.path.dirname(__file__)), './.minecraft/mods')
                shutil.rmtree(path)
                path = os.path.join(os.path.abspath(os.path.dirname(__file__)), './.minecraft/resourcepacks')
                shutil.rmtree(path)
                path = os.path.join(os.path.abspath(os.path.dirname(__file__)), './.minecraft/shaderpacks')
                shutil.rmtree(path)
                os.mkdir("./.minecraft/mods")
                os.mkdir("./.minecraft/resourcepacks")
                os.mkdir("./.minecraft/shaderpacks")

                self.assembly_mods()
                file2.close()

        file.close()

    def assembly_mods(self):
        file = open(assembly_m, "r")
        for files in file:
            if files == "mods:[\n":
                for files2 in file:
                    if files2 == "]\n":
                        break
                    files2 = files2.replace("\n", "")
                    files2 = "minecraft/mods/" + files2
                    print(files2)

                    file_path = Path(files2)
                    file_open = zipfile.ZipFile(files2, "r")
                    os.mkdir("./minecraft/imports")

                    file_open.extractall("./minecraft/imports")
                    file_zip = zipfile.ZipFile(f"./.minecraft/mods/" + file_path.name, "w")
                    for folder, subfolders, filest in os.walk("./minecraft/imports"):
                        for filer in filest:
                            file_zip.write(os.path.join(folder, filer),
                                           os.path.relpath(os.path.join(folder, filer), "./minecraft/imports"),
                                           compress_type=zipfile.ZIP_STORED)
                    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), './minecraft/imports')
                    shutil.rmtree(path)
                    file_open.close()

            if files == "textures:[\n":
                for files2 in file:
                    if files2 == "]\n":
                        break
                    files2 = files2.replace("\n", "")
                    files2 = "minecraft/textures/" + files2
                    print(files2)

                    file_path = Path(files2)
                    file_open = zipfile.ZipFile(files2, "r")
                    os.mkdir("./minecraft/imports")

                    file_open.extractall("./minecraft/imports")
                    file_zip = zipfile.ZipFile(f"./.minecraft/resourcepacks/" + file_path.name, "w")
                    for folder, subfolders, filest in os.walk("./minecraft/imports"):
                        for filer in filest:
                            file_zip.write(os.path.join(folder, filer),
                                           os.path.relpath(os.path.join(folder, filer), "./minecraft/imports"),
                                           compress_type=zipfile.ZIP_STORED)
                    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), './minecraft/imports')
                    shutil.rmtree(path)
                    file_open.close()


            if files == "shaders:[\n":
                for files2 in file:
                    if files2 == "]":
                        break
                    files2 = files2.replace("\n", "")
                    files2 = "minecraft/shaders/" + files2
                    print(files2)

                    file_path = Path(files2)
                    file_open = zipfile.ZipFile(files2, "r")
                    os.mkdir("./minecraft/imports")

                    file_open.extractall("./minecraft/imports")
                    file_zip = zipfile.ZipFile(f"./.minecraft/shaderpacks/" + file_path.name, "w")
                    for folder, subfolders, filest in os.walk("./minecraft/imports"):
                        for filer in filest:
                            file_zip.write(os.path.join(folder, filer),
                                           os.path.relpath(os.path.join(folder, filer), "./minecraft/imports"),
                                           compress_type=zipfile.ZIP_STORED)
                    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), './minecraft/imports')
                    shutil.rmtree(path)
                    file_open.close()
        file.close()
        file = open(assembly_m, "r")
        file.readline()
        vers = file.readline()
        vers = vers.replace("\n", "")
        vers = vers.replace("version:", "")
        file_v = open("version.info", "w")
        file_v.write(vers)
        self.label_3.setText(vers)
        file_v.close()
        file.close()
        self.Launch.start()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
