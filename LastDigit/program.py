__author__ = 'Sandi'
def r(a):
    m = {2: [2, 4, 8, 6],
         3: [3, 9, 7, 1],
         4: [4, 6],
         7: [7, 9, 3, 1],
         8: [8, 4, 2, 6],
         9: [9, 1]}

    return m[a]


def last_digit(n1, n2):
    return pow(n1, n2, 10)

assert last_digit(9, 7) == 9
assert last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651) == 7
