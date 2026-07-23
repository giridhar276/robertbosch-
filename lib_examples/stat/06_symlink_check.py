import os, stat
os.symlink("sample.txt", "sample_link.txt")
info = os.lstat("sample_link.txt")
print("Is symlink:", stat.S_ISLNK(info.st_mode))
os.remove("sample_link.txt")
