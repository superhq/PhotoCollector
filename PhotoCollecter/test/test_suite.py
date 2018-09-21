import unittest
from test.test_collector import TestCollector


if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [TestCollector("test_collector_less"),
             TestCollector('test_collector_more'),
             TestCollector("test_collector")]
    suite.addTests(tests)
    
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)