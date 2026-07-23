import os, stat
info = os.stat("sample.txt")
print("Full permission string:", stat.filemode(info.st_mode))
