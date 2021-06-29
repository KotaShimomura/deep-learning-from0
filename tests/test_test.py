import unittest

class TestTestCase(unittest.TestCase):
    """テストをするテストケース"""

    def test_add(self):
        expextied = 2
        actual = 1 + 1
        self.assertEqual(expextied, actual, msg="足し算が正しくありません")


if __name__ == '__main__':
    unittest.main()