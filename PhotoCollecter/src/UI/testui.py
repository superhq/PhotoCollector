from PyQt5.QtWidgets import QApplication
import sys
from mainwindow import MainWindow
from imgviewer import ImgViewer

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # win = ImgViewer()
    # win.show()
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
