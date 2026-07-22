import os
# Walk through a directory tree
for root, dirs, files in os.walk("."):
    print("Root:", root, "Dirs:", dirs, "Files:", files)
    break
