import filecmp
with open("cache1.txt", "w") as f:
    f.write("test")
with open("cache2.txt", "w") as f:
    f.write("test")
filecmp.cmp("cache1.txt", "cache2.txt")
filecmp.clear_cache()
print("Comparison cache cleared")
