# -*- coding:utf-8 -*-
import unittest
from collector import collector


class TestCollector(unittest.TestCase):

    def setUp(self):
        """
        在每个用例执行前执行
        """
        print('setup')

    def tearDown(self):
        """
        在每个用例执行后执行
        """
        print('tearDown')

    @classmethod
    def setUpClass(cls):
        """
        在所有用例执行前执行
        """
        print('create table')
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
    
    @unittest.skip('')    
    def test_collector_less(self):
        print('test less')
    @unittest.skip('')
    def test_collector_more(self):
        print('test more')
    
    def test_collector(self):
        col = collector()
        col.collect(r"D:\eclipse-java-photon-R-win32-x86_64")
        print("程序计数值为%d"%(col.count))


if __name__ == '__main__':
    unittest.main(verbosity=2)
