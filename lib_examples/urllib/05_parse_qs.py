from urllib.parse import parse_qs
query = "name=John&age=30&city=NY"
parsed = parse_qs(query)
print(parsed)
