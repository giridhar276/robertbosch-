import zipfile
with zipfile.ZipFile("archive.zip", "r") as zf:
    zf.extractall("extracted_folder")
print("Extracted all files")
