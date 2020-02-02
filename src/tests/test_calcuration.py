import unittest

# なんか素直にインポートできん。。
import sys
sys.path.append('/projects/src/')

from scripts import calcuration

env = 'prod'

class CalTest(unittest.TestCase):
    # テストの前にしたい処理
    def setUp(self):
        print('setup')
        self.cal = calcuration.Cal()

    # テストの後にしたい処理
    def tearDown(self):
        print('tearDown')
        del self.cal

    # 計算結果をテスト
    # @unittest.skip('skip this test')
    @unittest.skipIf(env=='prod', 'skip this test')
    def test_add_num_and_double(self):
        # cal = calcuration.Cal()
        self.assertEqual(self.cal.add_num_and_double(1, 1), 4)

    # Value Errorがあがるかをテスト
    # @unittest.skip('skip this test')
    def test_add_num_and_double_raise(self):
        # cal = calcuration.Cal()
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1', '1')


if __name__ == '__main__':
    unittest.main()
