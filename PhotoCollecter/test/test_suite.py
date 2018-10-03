import unittest
from test_collector import TestCollector
from test_calmd5 import TestCalDbMd5
from test_resorm import TestResOrm
from test_processor import TestProcessor
if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [TestCollector("test_collector_less"),
             TestCollector('test_collector_more'),
             TestCollector("test_collector"),
             TestCollector("test_subfix"),
             TestCalDbMd5("test_cal_db_md5"),
             TestResOrm("test_add_one"),
             TestResOrm("test_get_all"),
             TestResOrm('test_add'),
             TestProcessor('test_get_all_res')]
    suite.addTests(tests)
    
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)