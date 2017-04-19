def sub(st, sb):
    n = 0
    for i in range(len(st)):
        if st[i: i + len(sb)] == sb:
            n += 1
    return n
print(sub('ABCDCDC', 'CDC'))
