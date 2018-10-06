from res import Res, ResOperator
from fileinfo import FileInfo
import os


class Processor:
    def __init__(self, dest):
        self.resopt = ResOperator()
        self.fileinfo = FileInfo()
        self.dest = dest

    def process(self):
        items = self.resopt.get_all()
        n = 0
        for item in items:
            (datetime, maker, suffix) = self.fileinfo.getinfo(item.fullpath)
            name = ''
            topath = ''
            if datetime and suffix:
                name = datetime.replace(':', '_')
                if maker:
                    name = name + ' ' + maker + suffix
                else:
                    name = name + suffix
                topath = os.path.join(self.dest, name)

            self.resopt.update_uncommit(item.fullpath, datetime=datetime, maker=maker, suffix=suffix, topath=topath)
            n = n + 1
            if n % 100 == 0:
                self.resopt.commit()
        self.resopt.commit()
