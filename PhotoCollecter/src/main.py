import os
from collector import Collector
import res
import processor
from PyQt5.QtWidgets import QApplication
from UI.mainwindow import MainWindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    collector = Collector()
    win = MainWindow(collector)
    win.show()
    sys.exit(app.exec_())
    # col = collector.Collector()
    # col.collect(r"E:\20160610")
    # print(col.resopt.get_suffix_list())
    # proc = processor.Processor(dest=r'C:\Users\Qun\Desktop')
    # proc.process_dest_path()
    # proc.copy_read_files()
    # res_opt = res.ResOperator()
    # items = res_opt.get_all_unready()
    # for item in items:
    #     print(item)
