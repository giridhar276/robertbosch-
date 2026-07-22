import shutil, os
os.makedirs("src_dir", exist_ok=True)
with open("src_dir/data.txt", "w") as f:
    f.write("move me")
shutil.move("src_dir/data.txt", "moved_data.txt")
print("File moved")
