import unittest
from processor import Processor

#@unittest.skip('')
class TestProcessor(unittest.TestCase):
    def test_get_all_res(self):
        proc = Processor()
        proc.process()