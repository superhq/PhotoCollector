from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

from collector import Collector
from processor import Processor


# list dir and write file path into db
class CollectSourceTask(QObject):
    # 任务完成的信号
    done = pyqtSignal()

    def __init__(self, src):
        super().__init__()
        self.src = src
        self.collector = Collector()

    @pyqtSlot()
    def doWork(self):
        self.collector.collect(self.src)
        self.done.emit()


class CalculateDestinationTask(QObject):
    done = pyqtSignal()
    update = pyqtSignal(int, str)

    def __init__(self, dest):
        super().__init__()
        self.dest = dest

    @pyqtSlot()
    def doWork(self):
        self.processor = Processor()
        self.processor.setdest(self.dest)
        self.resopt = self.processor.resopt
        items = self.resopt.get_all_unready()
        n = 0
        for item in items:
            self.processor.process_dest_file(item)
            n = n + 1
            # 发送正在生成目标路径的信号
            self.update.emit(n, item.fullpath)
            if n % 100 == 0:
                self.resopt.commit()
        self.resopt.commit()
        self.done.emit()


class CopyTask(QObject):
    update = pyqtSignal(int, str)
    done = pyqtSignal()

    def __init__(self):
        super().__init__()

    def doWork(self):
        processor = Processor()
        n = 0
        for item in processor.resopt.get_all_ready():
            n = n + 1
            processor.copy_one_file(item.fullpath, item.topath)
            self.update.emit(n, item.fullpath)
        self.done.emit()
