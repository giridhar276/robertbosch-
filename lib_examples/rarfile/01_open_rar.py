import rarfile
# Requires the 'unrar' or 'unar' tool installed on the system, plus pip install rarfile
rf = rarfile.RarFile("archive.rar")
print("Opened archive.rar")
