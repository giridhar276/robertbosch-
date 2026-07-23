from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher = Fernet(key)
with open("plain.txt", "w") as f:
    f.write("Confidential file content")
with open("plain.txt", "rb") as f:
    data = f.read()
encrypted_data = cipher.encrypt(data)
with open("plain.txt.enc", "wb") as f:
    f.write(encrypted_data)
print("File encrypted")
