import unittest
from processor import Processor


#@unittest.skip('')
class TestProcessor(unittest.TestCase):
    def test_process(self):
        proc = Processor(dest = r'C:\Users\Qun\Desktop')
        proc.process_dest_path()
