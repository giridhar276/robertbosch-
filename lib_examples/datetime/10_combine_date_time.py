from datetime import date, time, datetime
d = date(2026, 7, 22)
t = time(14, 30, 0)
combined = datetime.combine(d, t)
print("Combined datetime:", combined)
