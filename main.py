# -*- coding: utf-8 -*-
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from ui.PageP import Ui_Form
from api.constants import data1, data2, data3, data4, data5


class MaPage(QMainWindow, Ui_Form):
    def __init__(self):
        super(MaPage, self).__init__()

        self.setupUi(self)
        self.connect()
        self.setWindowTitle("Pyside6")

    def connect(self, **kwargs):
        self.bt_analyse.clicked.connect(self.btn_analyse_go)

    def btn_analyse_go(self):
        self.textBrowser.append('Data1 : {}'.format(data1))
        self.textBrowser.append('Data2 : {}'.format(data2))
        self.textBrowser.append('Data3 : {}'.format(data3))
        self.textBrowser.append('Data4 : {}'.format(data4))
        self.textBrowser.append('Data5 : {}'.format(data5))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MaPage()
    window.show()
    sys.exit(app.exec())
