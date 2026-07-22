import time
time_string = "2026-07-22 10:00:00"
struct_time = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
epoch = time.mktime(struct_time)
print("Epoch from struct time:", epoch)
