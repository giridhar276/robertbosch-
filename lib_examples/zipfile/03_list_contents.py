import zipfile
with zipfile.ZipFile("archive.zip", "r") as zf:
    for name in zf.namelist():
        print(name)
