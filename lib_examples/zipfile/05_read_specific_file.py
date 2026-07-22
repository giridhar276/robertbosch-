import zipfile
with zipfile.ZipFile("archive.zip", "r") as zf:
    with zf.open("sample.txt") as f:
        content = f.read()
        print(content.decode())
