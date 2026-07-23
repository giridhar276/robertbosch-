import urllib.request
# Read content from a URL
with urllib.request.urlopen("https://www.python.org") as response:
    html = response.read(200)
    print(html)
