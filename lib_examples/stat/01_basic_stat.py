import os, stat
with open("sample.txt", "w") as f:
    f.write("data")
info = os.stat("sample.txt")
print("File mode:", stat.filemode(info.st_mode))
