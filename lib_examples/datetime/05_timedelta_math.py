from datetime import datetime, timedelta
now = datetime.now()
future = now + timedelta(days=10)
past = now - timedelta(days=5)
print("10 days from now:", future)
print("5 days ago:", past)
