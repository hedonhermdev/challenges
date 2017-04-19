#https://www.hackerrank.com/challenges/no-idea
happiness = 0

x, y = tuple(int(x) for x in input().split())

arr = [int(x) for x in input().split()]

s1 = set([int(x) for x in input().split()])
s2 = set([int(x) for x in input().split()])

for i in arr:
    if i in s1:
        happiness += 1
    elif i in s2:
        happiness += -1
print(happiness)