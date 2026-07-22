import os
# Get file stats via os.stat
with open("sample.txt", "w") as f:
    f.write("data")
info = os.stat("sample.txt")
print("Size:", info.st_size, "Modified:", info.st_mtime)
os.remove("sample.txt")
