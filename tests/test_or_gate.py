import unittest
from chapter02.or_gate import OR


class OrGateTestCase(unittest.TestCase):
    """ORゲートを確認するテストケース"""

    def test_true(self):
        expextied = 1
        actual = OR(1, 1)
        self.assertEqual(expextied, actual)

        expectied = 1
        actual = OR(0, 1)
        self.assertEqual(expectied, actual)

        expectied = 1
        actual = OR(1, 0)
        self.assertEqual(expectied, actual)

    def test_false(self):
        expectied = 0
        actual = OR(0, 0)
        self.assertEqual(expectied, actual)

if __name__ == '__main__':
    unittest.main()
