import zipfile
with zipfile.ZipFile("archive.zip", "r") as zf:
    bad_file = zf.testzip()
    print("Bad file found:", bad_file if bad_file else "None - zip is valid")
