import platform
lib, version = platform.libc_ver()
print("libc:", lib, "version:", version)
