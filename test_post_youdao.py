class PostYoudaoTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True,True)

    def test_get_ts(self):
        import time
        t=time.time()
        ts=str(int(round(t * 1000)))
        print(ts)
        get_ts=mock.Mok(return_value='1584684435788')
        self.assertEqual('1584684435788',get_ts())

if __name__=='__main__':
    unittest.main()