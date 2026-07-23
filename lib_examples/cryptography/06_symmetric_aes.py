from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
key = os.urandom(32)
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CFB(iv))
encryptor = cipher.encryptor()
ct = encryptor.update(b"Sensitive data") + encryptor.finalize()
print("AES ciphertext:", ct)
decryptor = cipher.decryptor()
pt = decryptor.update(ct) + decryptor.finalize()
print("Decrypted:", pt.decode())
