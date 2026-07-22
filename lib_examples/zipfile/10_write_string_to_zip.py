import zipfile
with zipfile.ZipFile("string_data.zip", "w") as zf:
    zf.writestr("info.txt", "This content was written directly as a string")
print("Created zip with in-memory string content")
