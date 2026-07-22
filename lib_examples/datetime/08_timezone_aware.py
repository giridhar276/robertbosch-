from datetime import datetime, timezone, timedelta
utc_now = datetime.now(timezone.utc)
ist = timezone(timedelta(hours=5, minutes=30))
ist_now = utc_now.astimezone(ist)
print("UTC time:", utc_now)
print("IST time:", ist_now)
