import shutil, os
# shutil.chown changes file owner/group (needs privileges); demonstrating copymode instead
with open("perm_src.txt", "w") as f:
    f.write("x")
with open("perm_dst.txt", "w") as f:
    f.write("y")
shutil.copymode("perm_src.txt", "perm_dst.txt")
print("Copied file permissions from perm_src.txt to perm_dst.txt")
