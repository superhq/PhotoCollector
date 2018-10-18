from Ui_ImgViewer import Ui_ImgViewer
from PyQt5.QtWidgets import QMainWindow,QFileDialog,QFileSystemModel
from PyQt5.QtCore import pyqtSlot,QDir
class ImgViewer(QMainWindow,Ui_ImgViewer):
    def __init__(self):
        super(QMainWindow,self).__init__()
        self.setupUi(self)
        self.rootdir = None
        self.model = QFileSystemModel()
        self.treeView.setModel(self.model)
        self.treeView.clicked.connect(self.on_file_clicked)

    @pyqtSlot()
    def on_file_clicked(self,*index):
        print(index)

    @pyqtSlot()
    def on_actionOpen_triggered(self):
        dialog = QFileDialog()
        result = dialog.getExistingDirectory()
        self.rootdir = result
        self.model.setRootPath(self.rootdir)
        self.treeView.setRootIndex(self.model.index(self.rootdir))


