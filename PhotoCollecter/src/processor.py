from res import Res, ResOperator
from fileinfo import FileInfo


class Processor:
    def __init__(self):
        self.resopt = ResOperator()
        self.fileinfo = FileInfo()

    def process(self):
        items = self.resopt.get_all()
        for item in items:
            (datetime, maker) = self.fileinfo.getinfo(item.fullpath)
            self.resopt.update_one(item.fullpath, datetime=datetime,maker=maker)

