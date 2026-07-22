import time
start = time.process_time()
sum(i * i for i in range(1000000))
end = time.process_time()
print("CPU process time:", end - start)
