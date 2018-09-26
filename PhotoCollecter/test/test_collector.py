# -*- coding:utf-8 -*-
import unittest
from collector import Collector


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
        col = Collector()
        col.db.create_table()


    @classmethod
    def tearDownClass(cls):
        """
         在所有用例执行后执行
        """
        col = Collector()
        print("数据库中一共有%d条记录" % (col.db.sum_rows()))
        print(col.db.sum_by_suffix())
        rows = col.db.select_unprocessed_file_with_filter(suffix_filter=('.png1', 'jpg'))
        for row in rows:
            print(row)
        print('drop table')

        col.db.drop_table()

    @unittest.skip('')
    def test_collector_less(self):
        print('test less')

    @unittest.skip('')
    def test_collector_more(self):
        print('test more')

    def test_collector(self):
        col = Collector()
        col.collect(r"C:\\")
        print("程序计数值为%d" % (col.count))

    @unittest.skip('')
    def test_subfix(self):
        col = Collector()
        print(col.suffix("abc.TXT"))
        print(col.suffix("./test_suite.py"))
        print(col.suffix(r"C:\Users\Qun\PycharmProjects\PhotoCollector\PhotoCollecter\test\test_suite.py"))


if __name__ == '__main__':
    unittest.main(verbosity=2)
