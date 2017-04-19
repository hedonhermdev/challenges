#https://www.hackerrank.com/challenges/finding-the-percentage
N = int(input())

dict = {}

for _ in range(N):
    arr = [x for x in input().split()]
    dict[arr[0]] = "%.2f" % (sum([float(x) for x in arr[1:]])/len(arr[1:]))
print(dict[input()])
