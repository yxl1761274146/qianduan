from unittest import mock

class PostYoudaoTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True,True)

    def test_get_ts(self):
        get_ts=mock.Mok(return_value='1584684435788')
        self.assertEqual('1584684435788',get_ts())

    def test_get_salt(self):
        get_salt=mock.Mok(return_value='15846848803956')
        self.asserEqual('15846848803956',get_salt())

if __name__=='__main__':
    unittest.main()