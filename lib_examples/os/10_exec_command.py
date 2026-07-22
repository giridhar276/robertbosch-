import os
# Run a shell command (os.system) and capture output (os.popen)
os.system("echo Hello from os.system")
output = os.popen("echo Hello from os.popen").read()
print(output.strip())
