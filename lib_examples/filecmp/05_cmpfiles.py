import filecmp, os
os.makedirs("cmp_dir1", exist_ok=True)
os.makedirs("cmp_dir2", exist_ok=True)
for name in ["a.txt", "b.txt"]:
    with open(f"cmp_dir1/{name}", "w") as f:
        f.write("match")
    with open(f"cmp_dir2/{name}", "w") as f:
        f.write("match")
match, mismatch, errors = filecmp.cmpfiles("cmp_dir1", "cmp_dir2", ["a.txt", "b.txt"])
print("Matched:", match, "Mismatched:", mismatch, "Errors:", errors)
