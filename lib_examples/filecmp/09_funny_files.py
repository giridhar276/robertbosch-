import filecmp, os
os.makedirs("funnyA", exist_ok=True)
os.makedirs("funnyB", exist_ok=True)
with open("funnyA/test.txt", "w") as f:
    f.write("data")
with open("funnyB/test.txt", "w") as f:
    f.write("data")
comparison = filecmp.dircmp("funnyA", "funnyB")
print("Files with comparison errors:", comparison.funny_files)
