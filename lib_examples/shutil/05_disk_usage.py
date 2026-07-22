import shutil
usage = shutil.disk_usage(".")
print("Total:", usage.total, "Used:", usage.used, "Free:", usage.free)
