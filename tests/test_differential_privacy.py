import unittest
from differential_privacy import add_noise
import numpy as np

class TestDifferentialPrivacy(unittest.TestCase):
    def setUp(self):
        self.data = np.array([1.0, 2.0, 3.0, 4.0])
        self.epsilon = 0.1

    def test_add_noise(self):
        noisy_data = add_noise(self.data, self.epsilon)
        self.assertEqual(len(noisy_data), len(self.data))
        self.assertNotEqual(list(noisy_data), list(self.data))

if __name__ == '__main__':
    unittest.main()
