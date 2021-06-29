import unittest
import numpy as np
from chapter03.relu import relu


class ReluTestCase(unittest.TestCase):
    """reluの機能テスト"""

    def test_representative(self):
        expected = 0.880797
        actual = relu(0.880797)
        self.assertAlmostEqual(expected, actual, places=6)

    def test_boundary(self):
        expexted = 0
        actual = relu(0)
        self.assertEqual(expexted, actual)

    def test_infinity(self):
        expected = float('inf')
        actual = relu(float('inf'))
        self.assertEqual(expected, actual)

    def test_supports_ndarray(self):
        expected = np.array([0, 0, 1])
        actual = relu(np.array([-1, 0, 1]))
        np.testing.assert_allclose(expected, actual)
