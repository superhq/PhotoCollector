# -*- coding:utf-8 -*-

import hashlib
from dbopt import dbopt
#计算md5值 
class calmd5():
    def __init__(self):
        pass
    def getmd5(self,path):
        m = hashlib.md5()
        with open(path,'rb') as f:
            
            m.update(f.read())
            ret = m.hexdigest()
        return ret


class CalDbMd5():

    def cal_db_md5(self):
        opt = dbopt()
        getmd5 = calmd5()
        rows = opt.select_unmd5_rows()
        for item in rows:
            file = item[0]
            md5 = getmd5.getmd5(file)
            opt.updatemd5(file, md5)
            print(file, md5)
