import time
utc_time = time.gmtime()
print("UTC time struct:", utc_time)
print("UTC formatted:", time.strftime("%Y-%m-%d %H:%M:%S", utc_time))
