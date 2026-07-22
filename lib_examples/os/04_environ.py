import os
# Read environment variables
path_var = os.environ.get("PATH")
print("PATH exists:", path_var is not None)
os.environ["MY_CUSTOM_VAR"] = "hello"
print(os.environ["MY_CUSTOM_VAR"])
