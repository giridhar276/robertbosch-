from cryptography.hazmat.primitives import hashes
digest = hashes.Hash(hashes.SHA256())
digest.update(b"data to hash")
digest.update(b" more data")
result = digest.finalize()
print("SHA256 hash:", result.hex())
