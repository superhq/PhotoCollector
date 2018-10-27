from res import Res, ResOperator
from fileinfo import PhotoInfo
from common import Status
import datetime
import os
import shutil





class Processor:
    def __init__(self):
        self.resopt = ResOperator()
        self.fileinfo = PhotoInfo()

    def setdest(self,dest):
        self.dest = dest

    def process_dest_file(self,item):
        (datestr, maker, suffix) = self.fileinfo.getinfo(item.fullpath)
        name = ''
        topath = ''
        status = Status.UNREADY
        if datestr and suffix:
            name = datestr.replace(':', '_')
            dateobj = datetime.datetime.strptime(datestr, '%Y:%m:%d %H:%M:%S')
            if maker:
                name = name + ' ' + maker + suffix
            else:
                name = name + suffix
            topath = os.path.join(self.dest, dateobj.year.__str__(), dateobj.month.__str__(), name)
            status = Status.REDAY
        self.resopt.update_uncommit(item.fullpath, status=status, datetime=datestr, maker=maker, suffix=suffix,
                                    topath=topath)
    def process_dest_path(self):
        items = self.resopt.get_all_unready()
        n = 0
        for item in items:
            # (datestr, maker, suffix) = self.fileinfo.getinfo(item.fullpath)
            # name = ''
            # topath = ''
            # status = Status.UNREADY
            # if datestr and suffix:
            #     name = datestr.replace(':', '_')
            #     dateobj = datetime.datetime.strptime(datestr,'%Y:%m:%d %H:%M:%S')
            #     if maker:
            #         name = name + ' ' + maker + suffix
            #     else:
            #         name = name + suffix
            #     topath = os.path.join(self.dest,dateobj.year.__str__(),dateobj.month.__str__(), name)
            #     status = Status.REDAY
            #
            # self.resopt.update_uncommit(item.fullpath, status=status, datetime=datestr, maker=maker, suffix=suffix, topath=topath)
            self.process_dest_file(item)
            n = n + 1
            if n % 100 == 0:
                self.resopt.commit()
        self.resopt.commit()

    def copy_read_files(self):
        items = self.resopt.get_all_ready()
        for res in items:
            base = os.path.dirname(res.topath)
            if os.path.exists(base) is False:
                os.makedirs(os.path.dirname(res.topath))
            shutil.copy(res.fullpath,res.topath)
            self.resopt.update_one(res.fullpath,status=Status.OK)
