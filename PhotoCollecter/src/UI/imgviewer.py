from Ui_ImgViewer import Ui_ImgViewer
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QFileSystemModel
from PyQt5.QtCore import pyqtSlot, QDir,QModelIndex,QRect
from PyQt5.QtGui import QPixmap


class ImgViewer(QMainWindow, Ui_ImgViewer):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.rootdir = None
        self.model = QFileSystemModel()
        self.treeView.setModel(self.model)
        self.treeView.activated.connect(self.on_file_clicked)

        self.maxwidth = 0
        self.maxheight = 0

    #显示之前，会调用resize,但这时得到的子控件大小可能是错的。
    def resizeEvent(self, *args, **kwargs):
        rect = self.imgView.geometry()
        (self.maxwidth,self.maxheight) = (rect.width(),rect.height())


    # 显示之前，会调用resize,但这时得到的子控件大小可能是错的。
    # 所以要在show中重新获取相关的大小
    def showEvent(self, *args, **kwargs):
        rect = self.imgView.geometry()
        (self.maxwidth, self.maxheight) = (rect.width(), rect.height())

    @pyqtSlot(QModelIndex)
    def on_file_clicked(self, index):
        fullpath = self.model.filePath(index)
        pixmap = QPixmap(fullpath)
        tmp = pixmap.scaledToHeight(self.maxheight)
        self.imgView.setPixmap(tmp)
        self.statusbar.showMessage(fullpath)

    @pyqtSlot()
    def on_actionOpen_triggered(self):
        dialog = QFileDialog()
        result = dialog.getExistingDirectory()
        self.rootdir = result
        self.model.setRootPath(self.rootdir)
        self.treeView.setRootIndex(self.model.index(self.rootdir))
