import zipfile
with open("file1.txt", "w") as f:
    f.write("File 1")
with open("file2.txt", "w") as f:
    f.write("File 2")
with zipfile.ZipFile("multi.zip", "w") as zf:
    zf.write("file1.txt")
    zf.write("file2.txt")
print("Added multiple files to multi.zip")
