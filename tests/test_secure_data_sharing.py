import unittest
from secure_data_sharing import secure_share, secure_receive
import seal
import numpy as np

class TestSecureDataSharing(unittest.TestCase):
    def setUp(self):
        self.context = seal.SEALContext.Create(seal.EncryptionParameters(seal.SchemeType.CKKS))
        self.data = np.array([1.0, 2.0, 3.0, 4.0])
        self.epsilon = 0.1

    def test_secure_share_receive(self):
        encrypted_data = secure_share(self.data, self.context, self.epsilon)
        decrypted_data = secure_receive(encrypted_data, self.context)
        self.assertEqual(len(decrypted_data), len(self.data))

if __name__ == '__main__':
    unittest.main()
