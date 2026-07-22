import zipfile
with zipfile.ZipFile("compressed.zip", "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
    zf.write("sample.txt")
print("Created compressed.zip with max compression")
