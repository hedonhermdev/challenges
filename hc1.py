#https://www.hackerrank.com/challenges/python-lists
N = int(input())

for i in range(N):
    arr = [int(x) for x in input().split()]
    ans = []
    result = arr[0]
    for j in range(arr[2]):
        result += (2 ** j) * arr[1]
        print(result)
        ans.append(result)
        print(ans)
    print(ans)

