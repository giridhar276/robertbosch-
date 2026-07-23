import os, stat
info = os.stat("sample.txt")
mode = info.st_mode
print("Owner readable:", bool(mode & stat.S_IRUSR))
print("Owner writable:", bool(mode & stat.S_IWUSR))
print("Owner executable:", bool(mode & stat.S_IXUSR))
