import unittest
from res import Res, ResOperator
import uuid


class TestResOrm(unittest.TestCase):
    @unittest.skip('')
    def test_add_one(self):
        opt = ResOperator()
        res = Res(fullpath=str(uuid.uuid4()), topath='to test')
        opt.add_one(res)
    @unittest.skip('')
    def test_get_all(self):
        opt = ResOperator()
        for res in opt.get_all():
            print(res)
    @unittest.skip('')
    def test_add(self):
        opt = ResOperator()
        res_list = []
        for i in range(10):
            res_list.append(Res(fullpath=str(uuid.uuid4())))
        opt.add(res_list)
