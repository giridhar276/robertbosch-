import os
info = os.stat("sample.txt")
print("Device ID:", info.st_dev)
print("Inode number:", info.st_ino)
print("Number of hard links:", info.st_nlink)
