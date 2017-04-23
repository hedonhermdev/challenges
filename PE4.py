import time
start = time.time()
arr = [x for x in range(998001, 10000, -1) if str(x)[::-1] == str(x)]
def ans():
    for x in arr:
        for i in range(999, 100, -1):
            if x % i == 0 and x//i <= 999 and x//i >= 100:
                return x, i, x//i
                break
print(ans())
print("Time taken: %f seconds" % (time.time() - start))