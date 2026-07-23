from urllib.parse import urljoin
base = "https://example.com/docs/page1.html"
relative = "../images/pic.png"
print(urljoin(base, relative))
