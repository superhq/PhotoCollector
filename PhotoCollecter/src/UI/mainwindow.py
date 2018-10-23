from Ui_MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow,QFileDialog
from PyQt5.QtChart import QChart,QPieSeries,QPieSlice
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPainter
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,collector = None):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.collector = collector
        self.srcEdit.setText(r'E:\20160610')
        self.chart = QChart()
        self.chart.setTheme(QChart.ChartThemeQt)
        self.chart.setTitle("文件类型统计")
        self.chartView.setChart(self.chart)

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

    @pyqtSlot(QPieSlice)
    def on_pieSeries_doubleliecked(self,slice):
        print(slice)

    @pyqtSlot()
    def on_collectPushButton_clicked(self):
        if self.collector:
            self.collector.collect(self.srcEdit.text())
            suffix_list = self.collector.resopt.get_suffix_list()
            self.chart.removeAllSeries()
            series = QPieSeries()
            for (suffix,count) in suffix_list:
                series.append(suffix,count)
            series.setLabelsVisible(True)

            self.chart.addSeries(series)


