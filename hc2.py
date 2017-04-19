#https://www.hackerrank.com/challenges/python-lists
if __name__ == '__main__':
    arr = []
    N = int(input())
    for i in range(N):
        i = input().split()
        if i[0] == 'insert':
            arr.insert(int(i[1]), int(i[2]))
        elif i[0] == 'print':
            print(arr)
        elif i[0] == 'remove':
            arr.remove(int(i[1]))
        elif i[0] == 'append':
            arr.append(int(i[1]))
        elif i[0] == 'sort':
            arr.sort()
        elif i[0] == 'pop':
            arr.remove(arr[-1])
        elif i[0] == 'reverse':
            arr.sort(reverse=True)
