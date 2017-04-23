import time

def triangular_seq1(e):
    arr = []
    elem = 0
    for i in range(e):
        elem += i
        arr.append(elem)
    return arr

def triangular_series(e):
    arr = []
    i = 1
    for i in range(10000, e):
        exp = i * (i + 1)//2
        arr.append(exp)
    return arr

start = time.time()
triangular_series(10**5)
print("ALG 1: %f" % (time.time() - start))

start = time.time()
triangular_seq1(10**5)
print("ALG 2: %f" %(time.time() - start))
