import filecmp
with open("shallow1.txt", "w") as f:
    f.write("data1")
with open("shallow2.txt", "w") as f:
    f.write("data2")
print("Shallow compare (metadata only):", filecmp.cmp("shallow1.txt", "shallow2.txt", shallow=True))
print("Deep compare (content):", filecmp.cmp("shallow1.txt", "shallow2.txt", shallow=False))
