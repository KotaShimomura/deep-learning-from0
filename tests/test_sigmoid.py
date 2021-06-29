import unittest
import numpy as np
from chapter03.sigmoid import sigmoid


class SigmoidTestCase(unittest.TestCase):
    """sigmoidの機能テスト"""

    def test_representative(self):
        expected = 0.880797
        actual = sigmoid(2)
        self.assertAlmostEqual(expected, actual, places=6)

        expected = 0.268941
        actual = sigmoid(-1)
        self.assertAlmostEqual(expected, actual, places=6)

    def test_infinity(self):
        expected = 1
        actual = sigmoid(float('inf'))
        self.assertEqual(expected, actual)

        expected = 0
        actual = sigmoid(-float('inf'))
        self.assertEqual(expected, actual)

    def test_supports_ndarray(self):
        expected = np.array([0.268941, 0.5, 0.731059])
        actual = sigmoid(np.array([-1, 0, 1]))
        np.testing.assert_allclose(expected, actual, atol=1e-6)
