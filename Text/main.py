# -*- coding:utf-8 -*-
# Author : JerryChu
from Text.textUi import Ui_MainWindow
from PyQt5 import QtWidgets
import sys


class Mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # 建立的是Main Window项目，故此处导入的是QMainWindow
    # 参考博客中建立的是Widget项目，因此哪里导入的是QWidget
    def __init__(self):
        super(Mywindow, self).__init__()
        self.setupUi(self)

    def addText(self):
        my_str=self.lineEdit.text()
        print(my_str)
        self.textEdit.append(my_str)
        self.lineEdit.setText('')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Mywindow()
    window.show()
    sys.exit(app.exec_())