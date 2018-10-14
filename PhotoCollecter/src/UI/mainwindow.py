from Ui_MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

    @pyqtSlot()
    def on_TestButton_clicked(self):
        print('clicked')
