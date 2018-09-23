#-*- coding:utf-8 -*-

from dbopt import dbopt
from calmd5 import calmd5
import os
#收集器。收集源路径中的所有文件的全路径，写入数据库。
class collector():
    def __init__(self):
        self.count = 0
        self.dbopt = dbopt()
        self.md5 = calmd5()
    
    def collect(self,path):
        """
        收集path目录下的所有文件，并将它们的全路径写入数据库
        """
        tmp = []

        for name in os.listdir(path):
            try:
                fullpath = os.path.join(path,name)
                if os.path.isdir(fullpath):
                    self.collect(fullpath)
                else:
                    tmp.append((fullpath,''))
                    print(fullpath)
                    self.count += 1
                    #每100个文件执行一次数据库操作
                    if len(tmp) == 100:
                        self.dbopt.insertfiles(tmp)
                        tmp.clear()
            except Exception as e:
                print(e)
        #将剩余的文件写入数据库
        self.dbopt.insertfiles(tmp)




