import os, stat
info = os.stat("sample.txt")
print("Is regular file:", stat.S_ISREG(info.st_mode))
print("Is directory:", stat.S_ISDIR(info.st_mode))
