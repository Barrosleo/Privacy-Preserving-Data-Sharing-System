from homomorphic_encryption import encrypt_data, decrypt_data
from differential_privacy import add_noise
import seal
import numpy as np

def secure_share(data, context, epsilon):
    noisy_data = add_noise(data, epsilon)
    encrypted_data = encrypt_data(noisy_data, context)
    return encrypted_data

def secure_receive(encrypted_data, context):
    decrypted_data = decrypt_data(encrypted_data, context)
    return decrypted_data

if __name__ == "__main__":
    context = seal.SEALContext.Create(seal.EncryptionParameters(seal.SchemeType.CKKS))
    data = np.array([1.0, 2.0, 3.0, 4.0])
    epsilon = 0.1
    encrypted_data = secure_share(data, context, epsilon)
    decrypted_data = secure_receive(encrypted_data, context)
    print(f"Original data: {data}")
    print(f"Decrypted data: {decrypted_data}")
