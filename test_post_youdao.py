import unittest
from unittest import mock

#from post_youdao import *

class PostYoudaoTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True,True)

    def test_get_ts(self):
        #import time
        #t=time.time()
        #ts=str(int(round(t * 1000)))
        #prrint(ts)
        get_ts=mock.Mock(return_value='1586498885563')
        self.assertEqual('1586498885563',get_ts())

    def test_get_salt(self):
        get_salt = mock.Mock(return_value='15864988855634')
        self.assertEqual('15864988855634',get_salt())

    def test_get_sign(self):
        get_sign=mock.Mock(return_value="")
        self.assertEqual('63ec4fac43e6d508ff508ab79a47cd11',get_sign())


if __name__=='__main__':
    unittest.main()
