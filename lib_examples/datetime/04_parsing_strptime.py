from datetime import datetime
date_string = "2026-07-22 15:30:00"
parsed = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed datetime:", parsed)
