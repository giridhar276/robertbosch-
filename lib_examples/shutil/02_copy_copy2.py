import shutil, os
os.makedirs("folder1", exist_ok=True)
with open("folder1/file.txt", "w") as f:
    f.write("data")
shutil.copy("folder1/file.txt", "folder1/file_copy.txt")
shutil.copy2("folder1/file.txt", "folder1/file_copy2.txt")
print("Files copied with copy and copy2")
