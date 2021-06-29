import unittest
from chapter02.nand_gate import NAND


class NandGateTestCase(unittest.TestCase):
    """ORゲートを確認するテストケース"""

    def test_true(self):
        expectied = 1
        actual = NAND(0, 1)
        self.assertEqual(expectied, actual)

        expectied = 1
        actual = NAND(1, 0)
        self.assertEqual(expectied, actual)

        expectied = 1
        actual = NAND(0, 0)
        self.assertEqual(expectied, actual)

    def test_false(self):
        expextied = 0
        actual = NAND(1, 1)
        self.assertEqual(expextied, actual)

if __name__ == '__main__':
    unittest.main()