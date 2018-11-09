from .Ui_MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtChart import QChart, QPieSeries
from PyQt5.QtCore import QThread
from .task import *
from res import ResOperator


# 图表显示的limit值要在界面参数化

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.resopt = ResOperator()
        self.chart = QChart()
        self.chart.setTheme(QChart.ChartThemeQt)
        self.chart.setTitle("文件类型统计")
        self.chartView.setChart(self.chart)
        self.progressBar.hide()

        self.collectSrcThread = None
        self.calDestThread = None
        self.copyThread = None

        self.collectSrcTask = None
        self.calDestTask = None
        self.copyTask = None

    @pyqtSlot()
    def show(self):
        super().show()
        print('show')



    # 在线程中已完成了文件的收集，在这里更新UI
    @pyqtSlot()
    def on_collect_finished(self):
        # 输出后缀统计扇形图
        suffix_list = self.resopt.get_suffix_list(5)
        all = self.resopt.count_all()
        self.chart.removeAllSeries()
        series = QPieSeries()
        for (suffix, count) in suffix_list:
            series.append(suffix, count)
            all -= count
        if all > 0:
            series.append('others', all)
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
        self.collectSrcTask = CollectSourceTask(self.srcEdit.text())
        # 将任务移入线程
        self.collectSrcThread = QThread()
        self.collectSrcTask.moveToThread(self.collectSrcThread)
        # 线程的started信号接入任务的doWork槽
        self.collectSrcThread.started.connect(self.collectSrcTask.doWork)
        # 任务完成信号(done)接入线程的quit槽
        self.collectSrcTask.done.connect(self.collectSrcThread.quit)
        # 线程完成后，更新ui
        self.collectSrcThread.finished.connect(self.on_collect_finished)
        # 启动
        self.collectSrcThread.start()

        # 根据收集的结果，开始处理文件

    @pyqtSlot()
    def on_processPushButton_clicked(self):
        count = self.resopt.count_all_unread()
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(count)
        self.progressBar.show()
        self.processPushButton.setDisabled(True)
        if self.destEdit.text() is not '':
            self.calDestTask = CalculateDestinationTask(self.destEdit.text())
            self.calDestThread = QThread()
            self.calDestTask.moveToThread(self.calDestThread)
            self.calDestThread.started.connect(self.calDestTask.doWork)
            self.calDestTask.done.connect(self.calDestThread.quit)
            self.calDestTask.update.connect(self.on_make_dest_running)
            self.calDestThread.finished.connect(self.on_make_dest_finished)
            self.calDestThread.start()

    # 开始复制文件
    @pyqtSlot()
    def on_copyPushButton_clicked(self):
        count = self.resopt.count_all_ready()
        if count:
            self.progressBar.show()
            self.progressBar.setValue(0)
            self.progressBar.setMinimum(0)
            self.progressBar.setMaximum(count)
            self.copyTask = CopyTask()
            self.copyThread = QThread()
            self.copyTask.moveToThread(self.copyThread)
            self.copyThread.started.connect(self.copyTask.doWork)
            self.copyTask.update.connect(self.on_copy_running)
            self.copyTask.done.connect(self.copyThread.quit)
            self.copyThread.finished.connect(self.on_copy_finished)
            self.copyThread.start()
