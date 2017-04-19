#https://www.hackerrank.com/challenges/nested-list
N = int(input())

arr = [[input(), float(input())] for _ in range(N)]
a2 = list(set([x[1] for x in arr]))
a2.sort()
lowest_grade = a2[1]
names = [x[0] for x in arr if x[1] == lowest_grade]
names.sort()
for i in names:
    print(i)

