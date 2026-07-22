import filecmp, os
os.makedirs("dirA", exist_ok=True)
os.makedirs("dirB", exist_ok=True)
with open("dirA/x.txt", "w") as f:
    f.write("x")
with open("dirB/x.txt", "w") as f:
    f.write("x")
with open("dirA/only_a.txt", "w") as f:
    f.write("a only")
comparison = filecmp.dircmp("dirA", "dirB")
print("Common files:", comparison.common_files)
print("Only in A:", comparison.left_only)
