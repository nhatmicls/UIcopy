import os, sys
from pathlib import Path
from typing import *

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog

parent_dir_path = str(Path(__file__).resolve().parents[2])
sys.path.append(parent_dir_path + "/UI/src/")

from UIcopy import Ui_MainWindow
from howtouse import Ui_howtouse


class howToUseApp(Ui_howtouse):
    def __init__(self, MainWindows) -> None:
        super().__init__()
        self.setupUi(MainWindows)


class App(Ui_MainWindow):
    def __init__(self, MainWindows) -> None:
        super().__init__()
        self.setupUi(MainWindows)
        self._set_interrupt()

    def _set_interrupt(self) -> None:
        """
        Add callback for object
        """

        self.howtouse_button.clicked.connect(self._howtouse_button_callback)
        self.brower_button.clicked.connect(self._browers_button_callback)
        self.backup_button.clicked.connect(self._backup_button_callback)
        self.clone_button.clicked.connect(self._clone_button_callback)

    def _browers_button_callback(self):
        file = QFileDialog.getExistingDirectory(
            None,
            caption="Open file",
            directory=parent_dir_path,
            options=QFileDialog.Option.ShowDirsOnly,
        )
        self.filepath_edit.setText(file)

    def _backup_button_callback(self):
        pass

    def _clone_button_callback(self):
        pass

    def _howtouse_button_callback(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.__new_window = howToUseApp(self.MainWindow)
        self.MainWindow.show()


def UIbuild():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = App(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    UIbuild()
