from datetime import datetime
now = datetime.now()
new_year = now.replace(month=1, day=1)
print("Modified date:", new_year)
print("ISO format:", now.isoformat())
