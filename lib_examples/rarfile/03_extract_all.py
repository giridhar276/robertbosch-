import rarfile
rf = rarfile.RarFile("archive.rar")
rf.extractall("extracted_rar")
print("Extracted all files from RAR archive")
