import unittest
from homomorphic_encryption import encrypt_data, decrypt_data
import seal
import numpy as np

class TestHomomorphicEncryption(unittest.TestCase):
    def setUp(self):
        self.context = seal.SEALContext.Create(seal.EncryptionParameters(seal.SchemeType.CKKS))
        self.data = [1.0, 2.0, 3.0, 4.0]

    def test_encrypt_decrypt(self):
        encrypted_data = encrypt_data(self.data, self.context)
        decrypted_data = decrypt_data(encrypted_data, self.context)
        np.testing.assert_almost_equal(self.data, decrypted_data, decimal=5)

if __name__ == '__main__':
    unittest.main()
