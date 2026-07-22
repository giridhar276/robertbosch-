import filecmp
with open("fileA.txt", "w") as f:
    f.write("content A")
with open("fileB.txt", "w") as f:
    f.write("content B")
result = filecmp.cmp("fileA.txt", "fileB.txt", shallow=False)
print("Files are identical:", result)
