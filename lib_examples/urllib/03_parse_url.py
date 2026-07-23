from urllib.parse import urlparse
result = urlparse("https://example.com/path?name=value&x=1")
print("Scheme:", result.scheme)
print("Netloc:", result.netloc)
print("Path:", result.path)
print("Query:", result.query)
