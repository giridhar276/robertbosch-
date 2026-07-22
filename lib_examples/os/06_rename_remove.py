import os
# Rename and remove a file
with open("a.txt", "w") as f:
    f.write("sample")
os.rename("a.txt", "b.txt")
print("Renamed a.txt to b.txt")
os.remove("b.txt")
print("Removed b.txt")
