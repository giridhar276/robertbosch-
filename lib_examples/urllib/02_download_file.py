import urllib.request
# Download a file from the web
url = "https://www.python.org/static/img/python-logo.png"
urllib.request.urlretrieve(url, "python_logo.png")
print("Downloaded python_logo.png")
