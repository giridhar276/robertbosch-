import filecmp, os
os.makedirs("dir1", exist_ok=True)
os.makedirs("dir2", exist_ok=True)
with open("dir1/common.txt", "w") as f:
    f.write("shared")
with open("dir2/common.txt", "w") as f:
    f.write("shared")
comparison = filecmp.dircmp("dir1", "dir2")
comparison.report()
