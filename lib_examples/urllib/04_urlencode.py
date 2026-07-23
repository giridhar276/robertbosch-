from urllib.parse import urlencode
params = {"q": "python tutorial", "page": 2}
encoded = urlencode(params)
print("Encoded query string:", encoded)
