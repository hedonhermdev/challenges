# Proving that number of zeroes in (10 ^ n)! where n >= 2is equal to [2.5 * 10 ^ n] - 1
def num_zeroes(num):
    z = 0
    n = 1
    while 5 ** n < num:
        z += (num // 5 ** n)
        n += 1
    return z
print(num_zeroes(140))
