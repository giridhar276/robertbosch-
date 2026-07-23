from cryptography.fernet import Fernet
# Use the same key that encrypted the file
key = Fernet.generate_key()  # replace with the actual saved key
cipher = Fernet(key)
with open("plain.txt.enc", "rb") as f:
    encrypted_data = f.read()
try:
    decrypted_data = cipher.decrypt(encrypted_data)
    print(decrypted_data.decode())
except Exception as e:
    print("Decryption failed (likely wrong key):", e)
