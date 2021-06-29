import unittest
from chapter02.xor_gate import XOR


class XorGateTestCase(unittest.TestCase):
    """ORゲートを確認するテストケース"""

    def test_true(self):
        expectied = 1
        actual = XOR(0, 1)
        self.assertEqual(expectied, actual)

        expectied = 1
        actual = XOR(1, 0)
        self.assertEqual(expectied, actual)

    def test_false(self):
        expectied = 0
        actual = XOR(0, 0)
        self.assertEqual(expectied, actual)

        expextied = 0
        actual = XOR(1, 1)
        self.assertEqual(expextied, actual)

if __name__ == '__main__':
    unittest.main()