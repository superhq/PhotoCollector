from Ui_MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtChart import QChart, QPieSeries, QPieSlice
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QThread, QObject
from PyQt5.QtGui import QPainter

from collector import Collector
from processor import Processor
from res import ResOperator


# 存在的问题
# 1.批量写数据库时不应该回滚
# 2.处理大量文件会自动退出
# ３.调试模式下正常，直接运行时收集功能不正常

class MainWindow(QMainWindow, Ui_MainWindow):
    # 自定义信号
    # 完成源路径文件的收集
    collect_thread_finished = pyqtSignal()
    # 完成目标路径的生成
    process_destpath_thread_finished = pyqtSignal()
    # 正在生成目录路径
    process_destpath_thread_running = pyqtSignal(int, str)

    class _CollectThread(QThread):
        def __init__(self, outer):
            super().__init__()
            self.collector = Collector()
            self.outer = outer
            self.finished.connect(self._finished)

        # 任务完成后向主线程发送已完成的信号
        @pyqtSlot()
        def _finished(self):
            self.outer.collect_thread_finished.emit()

        # 收集源路径下的所有文件
        def run(self):
            self.collector.collect(self.outer.srcEdit.text())

    class _CollectWorker(QObject):
        done = pyqtSignal()
        def __init__(self,cls_ui):
            super().__init__()
            self.cls_ui = cls_ui
            self.collector = Collector()

        @pyqtSlot()
        def doWork(self):
            self.collector.collect(self.cls_ui.srcEdit.text())
            #self.emit(self.done)
            self.cls_ui.collect_thread_finished.emit()


    class _ProcessDestPath(QThread):
        def __init__(self, outer):
            super().__init__()
            self.outer = outer
            self.processor = None

        def run(self):
            self.resopt = ResOperator()
            self.processor = Processor()
            self.processor.setdest(self.outer.destEdit.text())
            items = self.resopt.get_all_unready()
            n = 0
            for item in items:
                self.processor.process_dest_file(item)
                n = n + 1
                # 发送正在生成目标路径的信号
                self.outer.process_destpath_thread_running.emit(n, item.fullpath)
                if n % 100 == 0:
                    self.resopt.commit()
            self.resopt.commit()

    def __init__(self, collector=None):
        super(MainWindow, self).__init__()

        self.setupUi(self)
        self.collector = collector
        self.resopt = ResOperator()
        self.srcEdit.setText(r'E:\20160610')
        self.chart = QChart()
        self.chart.setTheme(QChart.ChartThemeQt)
        self.chart.setTitle("文件类型统计")
        self.chartView.setChart(self.chart)
        self.progressBar.hide()
        # 收集线程
        # self.collectWorker = MainWindow._CollectWorker(self)
        # self.collectWorkerThread = QThread()
        # self.collectWorker.moveToThread(self.collectWorkerThread)
        # self.collectWorkerThread.started.connect(self.collectWorker.doWork)

        # self.collect_thread = MainWindow._CollectThread(self)
        # self.collect_thread_finished.connect(self.on_collect_thread_finished)
        # self.process_destpath_thread = MainWindow._ProcessDestPath(self)
        # self.process_destpath_thread_running.connect(self.on_process_destpath_thread_running)
        self.collect_thread_finished.connect(self.on_collect_thread_finished)

    # 在线程中已完成了文件的收集，在这里更新UI
    @pyqtSlot()
    def on_collect_thread_finished(self):
        # 输出后缀统计扇形图
        suffix_list = self.resopt.get_suffix_list()
        self.chart.removeAllSeries()
        series = QPieSeries()
        for (suffix, count) in suffix_list:
            series.append(suffix, count)
            series.setLabelsVisible(True)
        self.chart.addSeries(series)
        # 设置按键和进度条
        self.collectPushButton.setEnabled(True)
        self.progressBar.hide()

    @pyqtSlot()
    def on_process_destpath_thread_finished(self):
        pass

    # 正在生成目标文件路径
    @pyqtSlot(int, str)
    def on_process_destpath_thread_running(self, count, path):
        self.progressBar.setValue(count)
        self.progressLabel.setText(path)

    # 选择源路径
    @pyqtSlot()
    def on_srcPushButton_clicked(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            self.srcEdit.setText(dialog.selectedFiles()[0])

    # 根据收集的结果，开始处理文件
    @pyqtSlot()
    def on_processPushButton_clicked(self):
        count = self.resopt.count_all_unread()
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(count)
        self.progressBar.show()
        if self.destEdit.text() is not '':
            self.process_destpath_thread.start()

    # 选择目标路径
    @pyqtSlot()
    def on_destPushButton_clicked(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            self.destEdit.setText(dialog.selectedFiles()[0])


    # 开始收集源路径中的文件
    @pyqtSlot()
    def on_collectPushButton_clicked(self):
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        self.progressBar.show()
        # self.collectPushButton.setDisabled(True)
        # self.collect_thread.start()
        self.collectWorker = MainWindow._CollectWorker(self)
        self.collectWorkerThread = QThread()
        self.collectWorker.moveToThread(self.collectWorkerThread)
        self.collectWorkerThread.started.connect(self.collectWorker.doWork)
        self.collectWorkerThread.start()

