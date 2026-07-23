import os, stat
os.chmod("sample.txt", stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)
info = os.stat("sample.txt")
print("Is executable by owner:", bool(info.st_mode & stat.S_IXUSR))
