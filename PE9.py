import time
from math import sqrt
# Brute Force
#Takes ~22 seconds
def pythagorean_triplet1(perimeter):
    for i in range(1, perimeter):
        for j in range(1, perimeter):
            for k in range(1, perimeter):
                if i + j + k == perimeter and sqrt(i ** 2 + j**2) == k:
                    return i, j, k


# Euclid's Formula
#Takes less than 0.1 second.
def pythagorean_triplet2(perimeter):
    for m in range(1, perimeter - 1):
        for n in range(1, perimeter - m):
            a = 2 * m * n
            b = abs(m ** 2 - n ** 2)
            c = abs(m ** 2 + n ** 2)
            if a + b + c == perimeter:
                return a, b, c

start = time.time()
print("ALG 1")
# print("Ans:", pythagorean_triplet1(1000))
print("Time Taken: %f" % (time.time() - start))
start = time.time()
print("ALG 2")
print("Ans:", pythagorean_triplet2(1000))
print("Time Taken: %f" % (time.time() - start))
