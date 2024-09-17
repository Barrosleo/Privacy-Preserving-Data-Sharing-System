import seal
import numpy as np

def encrypt_data(data, context):
    encoder = seal.CKKSEncoder(context)
    encryptor = seal.Encryptor(context, context.key_context_data().parms_id())
    plain = seal.Plaintext()
    encoder.encode(data, context.scale(), plain)
    encrypted = seal.Ciphertext()
    encryptor.encrypt(plain, encrypted)
    return encrypted

def decrypt_data(encrypted, context):
    decryptor = seal.Decryptor(context, context.key_context_data().parms_id())
    plain = seal.Plaintext()
    decryptor.decrypt(encrypted, plain)
    encoder = seal.CKKSEncoder(context)
    result = np.zeros(encoder.slot_count())
    encoder.decode(plain, result)
    return result

if __name__ == "__main__":
    context = seal.SEALContext.Create(seal.EncryptionParameters(seal.SchemeType.CKKS))
    data = [1.0, 2.0, 3.0, 4.0]
    encrypted_data = encrypt_data(data, context)
    decrypted_data = decrypt_data(encrypted_data, context)
    print(f"Original data: {data}")
    print(f"Decrypted data: {decrypted_data}")
