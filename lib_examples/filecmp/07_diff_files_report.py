import filecmp, os
os.makedirs("diffA", exist_ok=True)
os.makedirs("diffB", exist_ok=True)
with open("diffA/data.txt", "w") as f:
    f.write("version 1")
with open("diffB/data.txt", "w") as f:
    f.write("version 2")
comparison = filecmp.dircmp("diffA", "diffB")
print("Files that differ:", comparison.diff_files)
