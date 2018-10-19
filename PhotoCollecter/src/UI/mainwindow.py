from Ui_MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow,QFileDialog
from PyQt5.QtChart import QChart,QBarSeries,QBarSet,QBarCategoryAxis
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPainter
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,collector = None):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.collector = collector
        self.srcEdit.setText(r'E:\20160610')
        chart = QChart()
        chart.setTitle('文件统计')
        self.chart.setChart(chart)

    @pyqtSlot()
    def on_srcPushButton_clicked(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            self.srcEdit.setText(dialog.selectedFiles()[0])
    @pyqtSlot()
    def on_destPushButton_clicked(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            self.destEdit.setText(dialog.selectedFiles()[0])

    @pyqtSlot()
    def on_collectPushButton_clicked(self):
        if self.collector:
            self.collector.collect(self.srcEdit.text())
            suffix_list = self.collector.resopt.get_suffix_list()
            chart = QChart()
            chart.setTitle('文件统计')
            series = QBarSeries()
            for (suffix,count) in suffix_list:

                qset = QBarSet(suffix)
                qset.append(count)
                series.append(qset)
            chart.addSeries(series)

            axis = QBarCategoryAxis()
            for (suffix,_) in suffix_list:
                axis.append(suffix)
            chart.setAnimationOptions(QChart.SeriesAnimations)
            chart.createDefaultAxes()
            chart.setAxisX(axis,series)
            chart.legend().setVisible(True)
            self.chart.setChart(chart)
            self.chart.setRenderHint(QPainter.Antialiasing)


