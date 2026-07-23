import os
info = os.stat("sample.txt")
print("Size in bytes:", info.st_size)
print("Last modified time:", info.st_mtime)
print("Last accessed time:", info.st_atime)
