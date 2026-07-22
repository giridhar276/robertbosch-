import time
def slow_function():
    total = 0
    for i in range(500000):
        total += i
    return total

start = time.time()
slow_function()
end = time.time()
print(f"Function took {end - start:.4f} seconds")
