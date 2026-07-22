import zipfile
with zipfile.ZipFile("archive.zip", "r") as zf:
    zf.extract("sample.txt", "single_extract")
print("Extracted sample.txt")
