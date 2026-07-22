import rarfile
rf = rarfile.RarFile("archive.rar")
for name in rf.namelist():
    print(name)
