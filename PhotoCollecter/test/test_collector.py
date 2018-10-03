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
        pass



    @classmethod
    def tearDownClass(cls):
        """
         在所有用例执行后执行
        """
        pass

    @unittest.skip('')
    def test_collector_less(self):
        print('test less')

    @unittest.skip('')
    def test_collector_more(self):
        print('test more')

    @unittest.skip('')
    def test_collector(self):
        col = Collector()
        col.collect(r"E:\\huawei-20151212")
        print("程序计数值为%d" % (col.count))

    @unittest.skip('')
    def test_subfix(self):
        col = Collector()
        print(col.suffix("abc.TXT"))
        print(col.suffix("./test_suite.py"))
        print(col.suffix(r"C:\Users\Qun\PycharmProjects\PhotoCollector\PhotoCollecter\test\test_suite.py"))


if __name__ == '__main__':
    unittest.main(verbosity=2)
