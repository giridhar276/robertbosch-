import os
# Build and split paths
full_path = os.path.join("home", "user", "file.txt")
print("Joined:", full_path)
print("Split:", os.path.split(full_path))
print("Basename:", os.path.basename(full_path))
print("Dirname:", os.path.dirname(full_path))
