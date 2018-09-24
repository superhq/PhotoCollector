# -*- coding:utf-8 -*-

from dbopt import DbOpt
from calmd5 import Md5Tools
import os


# 收集器。收集源路径中的所有文件的全路径，写入数据库。
class Collector:
    def __init__(self):
        self.count = 0
        self.db = DbOpt()
        self.md5 = Md5Tools()

    def suffix(self, fname):
        """
        获取文件的后缀
        :param fname: 文件名
        :return: 返回文件的后缀
        """
        return os.path.splitext(fname)[-1].lower()

    def collect(self, path):
        """
        收集path目录下的所有文件，并将它们的全路径写入数据库
        """
        tmp = []

        for name in os.listdir(path):
            try:
                fullpath = os.path.join(path, name)
                if os.path.isdir(fullpath):
                    self.collect(fullpath)
                else:
                    tmp.append((fullpath,self.suffix(name), ''))
                    print(fullpath)
                    self.count += 1
                    # 每100个文件执行一次数据库操作
                    if len(tmp) == 100:
                        self.db.insertfiles(tmp)
                        tmp.clear()
            except Exception as e:
                print(e)
        # 将剩余的文件写入数据库
        self.db.insertfiles(tmp)
