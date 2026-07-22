import shutil, os
os.makedirs("tree_src/sub", exist_ok=True)
with open("tree_src/sub/f.txt", "w") as f:
    f.write("x")
shutil.copytree("tree_src", "tree_dst")
print("Tree copied")
shutil.rmtree("tree_dst")
print("Tree removed")
