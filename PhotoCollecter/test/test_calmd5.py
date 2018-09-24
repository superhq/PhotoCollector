import unittest

from collector import  Collector
from calmd5 import CalDbMd5
from dbopt import DbOpt

@unittest.skip("")
class TestCalDbMd5(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        col = Collector()
        col.db.create_table()

    @classmethod
    def tearDownClass(cls):
        """
         在所有用例执行后执行
        """
        col = Collector()
        print("数据库中一共有%d条记录" % (col.db.sum_rows()))
        print('drop table')

        col.db.drop_table()

    def test_cal_db_md5(self):
        col = Collector()
        col.collect(r'E:\xixi&hanhan')
        obj = CalDbMd5()
        obj.cal_db_md5()