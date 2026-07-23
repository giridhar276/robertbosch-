from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher = Fernet(key)
token = cipher.encrypt(b"Secret message")
print("Encrypted:", token)
decrypted = cipher.decrypt(token)
print("Decrypted:", decrypted.decode())
