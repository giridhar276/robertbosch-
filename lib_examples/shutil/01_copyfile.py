import shutil
with open("source.txt", "w") as f:
    f.write("hello")
shutil.copyfile("source.txt", "dest.txt")
print("Copied source.txt to dest.txt")
