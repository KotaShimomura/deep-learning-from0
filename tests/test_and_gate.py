import unittest
from chapter02.and_gate import AND


class AndGateTestCase(unittest.TestCase):
    """ANDゲートを確認するテストケース"""

    def test_true(self):
        expextied = 1
        actual = AND(1, 1)
        self.assertEqual(expextied, actual)

    def test_false(self):
        expectied = 0
        actual = AND(0, 0)
        self.assertEqual(expectied, actual)

        expectied = 0
        actual = AND(0, 1)
        self.assertEqual(expectied, actual)

        expectied = 0
        actual = AND(1, 0)
        self.assertEqual(expectied, actual)


if __name__ == '__main__':
    unittest.main()
