from .Ui_MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtChart import QChart, QPieSeries, QPieSlice
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QThread, QObject
from PyQt5.QtGui import QPainter

from collector import Collector
from processor import Processor
from res import ResOperator


# 存在的问题

# 2.处理大量文件会自动退出


class MainWindow(QMainWindow, Ui_MainWindow):
    # # 自定义信号
    # # 完成源路径文件的收集
    # collect_finished = pyqtSignal()
    # # 完成目标路径的生成
    # make_dest_finished = pyqtSignal()
    # # 正在生成目录路径
    # make_dest_running = pyqtSignal(int, str)

    class _CollectTask(QObject):
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

    class _MakeDestTask(QObject):
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

    class _CopyTask(QObject):
        update = pyqtSignal(int, str)
        done = pyqtSignal()

        def __init__(self):
            super().__init__()

        def doWork(self):
            processor = Processor()
            n = 0
            for item in processor.resopt.get_all_ready():
                n = n + 1
                processor.copy_one_file(item.fullpath,item.topath)
                self.update.emit(n, item.fullpath)
            self.done.emit()

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
        self.collectThread = None
        self.makeDestThread = None
        self.copyThread = None

    # 在线程中已完成了文件的收集，在这里更新UI
    @pyqtSlot()
    def on_collect_finished(self):
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
    def on_copy_finished(self):
        self.progressLabel.setText("完成复制")

    @pyqtSlot()
    def on_make_dest_finished(self):
        self.processPushButton.setEnabled(True)

    # 正在生成目标文件路径
    @pyqtSlot(int, str)
    def on_make_dest_running(self, count, path):
        self.progressBar.setValue(count)
        self.progressLabel.setText("计算目标路径:" + path)

    # 正在复制文件
    def on_copy_running(self, count, path):
        self.progressBar.setValue(count)
        self.progressLabel.setText("复制文件:" + path)

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
        self.processPushButton.setDisabled(True)
        if self.destEdit.text() is not '':
            # self.process_destpath_thread.start()
            self.makeDestTask = MainWindow._MakeDestTask(self.destEdit.text())
            self.makeDestThread = QThread()
            self.makeDestTask.moveToThread(self.makeDestThread)
            self.makeDestThread.started.connect(self.makeDestTask.doWork)
            self.makeDestTask.done.connect(self.makeDestThread.quit)
            self.makeDestTask.update.connect(self.on_make_dest_running)
            self.makeDestThread.finished.connect(self.on_make_dest_finished)
            self.makeDestThread.start()

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
        # 设置UI
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        self.progressBar.show()
        self.collectPushButton.setDisabled(True)
        # 创建任务
        self.collectWorker = MainWindow._CollectTask(self.srcEdit.text())
        # 将任务移入线程
        self.collectThread = QThread()
        self.collectWorker.moveToThread(self.collectThread)
        # 线程的started信号接入任务的doWork槽
        self.collectThread.started.connect(self.collectWorker.doWork)
        # 任务完成信号(done)接入线程的quit槽
        self.collectWorker.done.connect(self.collectThread.quit)
        # 线程完成后，更新ui
        self.collectThread.finished.connect(self.on_collect_finished)
        # 启动
        self.collectThread.start()

    # 开始复制文件
    @pyqtSlot()
    def on_copyPushButton_clicked(self):
        count = self.resopt.count_all_ready()
        if count:
            self.progressBar.show()
            self.progressBar.setValue(0)
            self.progressBar.setMinimum(0)
            self.progressBar.setMaximum(count)
            self.copyWorker = MainWindow._CopyTask()
            self.copyThread = QThread()
            self.copyWorker.moveToThread(self.copyThread)
            self.copyThread.started.connect(self.copyWorker.doWork)
            self.copyWorker.update.connect(self.on_copy_running)
            self.copyWorker.done.connect(self.copyThread.quit)
            self.copyThread.finished.connect(self.on_copy_finished)
            self.copyThread.start()
