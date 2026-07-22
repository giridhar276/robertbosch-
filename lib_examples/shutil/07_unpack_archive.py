import shutil, os
os.makedirs("unpack_dest", exist_ok=True)
shutil.unpack_archive("my_archive.zip", "unpack_dest")
print("Archive unpacked to unpack_dest")
