# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './generate/UIcopy.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(544, 172)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.filepath_label = QtWidgets.QLabel(self.centralwidget)
        self.filepath_label.setGeometry(QtCore.QRect(10, 10, 51, 21))
        self.filepath_label.setObjectName("filepath_label")
        self.filepath_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.filepath_edit.setGeometry(QtCore.QRect(70, 10, 381, 22))
        self.filepath_edit.setObjectName("filepath_edit")
        self.maincharacter_label = QtWidgets.QLabel(self.centralwidget)
        self.maincharacter_label.setGeometry(QtCore.QRect(10, 50, 91, 21))
        self.maincharacter_label.setObjectName("maincharacter_label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(100, 50, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.brower_button = QtWidgets.QPushButton(self.centralwidget)
        self.brower_button.setGeometry(QtCore.QRect(460, 10, 75, 24))
        self.brower_button.setObjectName("brower_button")
        self.backup_button = QtWidgets.QPushButton(self.centralwidget)
        self.backup_button.setGeometry(QtCore.QRect(230, 110, 101, 31))
        self.backup_button.setObjectName("backup_button")
        self.clone_button = QtWidgets.QPushButton(self.centralwidget)
        self.clone_button.setGeometry(QtCore.QRect(400, 110, 101, 31))
        self.clone_button.setObjectName("clone_button")
        self.howtouse_button = QtWidgets.QPushButton(self.centralwidget)
        self.howtouse_button.setGeometry(QtCore.QRect(50, 110, 101, 31))
        self.howtouse_button.setObjectName("howtouse_button")
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setGeometry(QtCore.QRect(290, 50, 41, 21))
        self.status_label.setObjectName("status_label")
        self.status_state = QtWidgets.QLabel(self.centralwidget)
        self.status_state.setGeometry(QtCore.QRect(330, 50, 91, 21))
        self.status_state.setObjectName("status_state")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 544, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UICopy"))
        self.filepath_label.setText(_translate("MainWindow", "File path:"))
        self.maincharacter_label.setText(_translate("MainWindow", "Main character:"))
        self.brower_button.setText(_translate("MainWindow", "Brower"))
        self.backup_button.setText(_translate("MainWindow", "Backup"))
        self.clone_button.setText(_translate("MainWindow", "Clone"))
        self.howtouse_button.setText(_translate("MainWindow", "How to use"))
        self.status_label.setText(_translate("MainWindow", "Status:"))
        self.status_state.setText(_translate("MainWindow", "Unknown"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())