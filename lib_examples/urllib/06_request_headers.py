import urllib.request
req = urllib.request.Request(
    "https://www.python.org",
    headers={"User-Agent": "Mozilla/5.0"}
)
with urllib.request.urlopen(req) as response:
    print("Status:", response.status)
