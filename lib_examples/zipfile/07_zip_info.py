import zipfile
with zipfile.ZipFile("archive.zip", "r") as zf:
    for info in zf.infolist():
        print(info.filename, info.file_size, info.date_time)
