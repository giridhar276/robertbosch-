import os, stat
os.makedirs("stat_test_dir", exist_ok=True)
info = os.stat("stat_test_dir")
print("Is a directory:", stat.S_ISDIR(info.st_mode))
os.rmdir("stat_test_dir")
