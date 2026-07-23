import os, stat
os.chmod("sample.txt", stat.S_IRUSR | stat.S_IWUSR)
print("Permissions changed to read/write for owner only")
info = os.stat("sample.txt")
print("New mode:", stat.filemode(info.st_mode))
