from PyQt5.QtWidgets import QApplication
from UI.mainwindow import MainWindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
