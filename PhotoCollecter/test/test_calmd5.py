import unittest

from collector import  collector
from calmd5 import CalDbMd5
from dbopt import dbopt


class TestCalDbMd5(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        col = collector()
        col.dbopt.create_table()

    @classmethod
    def tearDownClass(cls):
        """
         在所有用例执行后执行
        """
        col = collector()
        print("数据库中一共有%d条记录"%(col.dbopt.sum_rows()))
        print('drop table')

        col.dbopt.drop_table()

    def test_cal_db_md5(self):
        col = collector()
        col.collect(r'E:\xixi&hanhan')
        obj = CalDbMd5()
        obj.cal_db_md5()