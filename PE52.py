def ans():
    i = 1
    while True:
        arr = []
        for x in range(1, 7):
            arr.append(sorted((int(x) for x in str(i * x))))
        print(arr)
        if all(x == arr[0] for x in arr):
            return i
        i += 1
print(ans())

