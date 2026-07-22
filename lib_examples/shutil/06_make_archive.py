import shutil, os
os.makedirs("archive_src", exist_ok=True)
with open("archive_src/a.txt", "w") as f:
    f.write("archive me")
shutil.make_archive("my_archive", "zip", "archive_src")
print("Archive created: my_archive.zip")
