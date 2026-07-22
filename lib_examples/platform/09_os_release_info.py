import platform
print("Version:", platform.version())
try:
    print("Distribution info:", platform.freedesktop_os_release())
except Exception as e:
    print("Could not read OS release info:", e)
