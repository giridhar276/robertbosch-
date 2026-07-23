import urllib.request
import urllib.error
try:
    urllib.request.urlopen("https://www.python.org/this-does-not-exist")
except urllib.error.HTTPError as e:
    print("HTTP Error:", e.code, e.reason)
except urllib.error.URLError as e:
    print("URL Error:", e.reason)
