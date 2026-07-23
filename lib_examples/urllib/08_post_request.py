import urllib.request
import urllib.parse
data = urllib.parse.urlencode({"key": "value"}).encode()
req = urllib.request.Request("https://httpbin.org/post", data=data, method="POST")
with urllib.request.urlopen(req) as response:
    print("Status:", response.status)
