import filecmp, os
os.makedirs("nested1/sub", exist_ok=True)
os.makedirs("nested2/sub", exist_ok=True)
with open("nested1/sub/f.txt", "w") as f:
    f.write("hello")
with open("nested2/sub/f.txt", "w") as f:
    f.write("hello")
comparison = filecmp.dircmp("nested1", "nested2")
comparison.report_full_closure()
