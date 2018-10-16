from Ui_ImgViewer import Ui_ImgViewer
from PyQt5.QtWidgets import QMainWindow,QFileDialog
from PyQt5.QtCore import pyqtSlot
class ImgViewer(QMainWindow,Ui_ImgViewer):
    def __init__(self):
        super(QMainWindow,self).__init__()
        self.setupUi(self)


    @pyqtSlot()
    def on_actionOpen_triggered(self):
        dialog = QFileDialog()
        result = dialog.exec_()
        if result == QFileDialog.Accepted:
            print(dialog.selectedFiles()[0])