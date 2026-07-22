import time
start = time.perf_counter()
total = sum(range(1000000))
end = time.perf_counter()
print("Elapsed time:", end - start, "seconds")
