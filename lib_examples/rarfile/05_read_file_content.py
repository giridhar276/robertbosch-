import rarfile
rf = rarfile.RarFile("archive.rar")
with rf.open("sample.txt") as f:
    content = f.read()
    print(content.decode())
