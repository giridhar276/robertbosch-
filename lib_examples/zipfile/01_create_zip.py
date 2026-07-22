import zipfile
with open("sample.txt", "w") as f:
    f.write("Hello Zip")
with zipfile.ZipFile("archive.zip", "w") as zf:
    zf.write("sample.txt")
print("Created archive.zip")
