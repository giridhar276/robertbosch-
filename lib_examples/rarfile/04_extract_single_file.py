import rarfile
rf = rarfile.RarFile("archive.rar")
rf.extract("sample.txt", "single_extract_rar")
print("Extracted sample.txt from RAR")
