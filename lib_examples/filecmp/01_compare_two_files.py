import filecmp
with open("file1.txt", "w") as f:
    f.write("same content")
with open("file2.txt", "w") as f:
    f.write("same content")
result = filecmp.cmp("file1.txt", "file2.txt")
print("Files are identical:", result)
