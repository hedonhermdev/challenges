#https://www.hackerrank.com/challenges/py-set-discard-remove-pop
n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    i = input().split()
    if len(i) == 2:
        i[1] = int(i[1])

    if i[0] == 'pop':
        s.pop()
    elif i[0] == 'remove':
        s.remove(i[1])
    elif i[0] == 'discard':
        s.discard(i[1])
print(sum(s))
