#https://www.hackerrank.com/challenges/symmetric-difference

N = int(input())
s1 = set([int(x) for x in input().split()])
M = int(input())
s2 = set([int(x) for x in input().split()])
u = s1.union(s2)
for i in s1.intersection(s2):
    u.discard(i)
for e in sorted(list(u)):
    print(e)

