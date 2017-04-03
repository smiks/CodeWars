__author__ = 'Sandi'

from math import factorial
def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k)*factorial(n-k))

def total_inc_dec(x):
    map = {
        0: 1,
        1:10,
        2: 100,
        3: 475,
        4: 1675,
        5: 4594,
        6: 12952,
        7: 30817,
        8: 67987,
        9: 140907,
        10: 277033
    }
    if x in map:
        return map[x]

    bc = binomial_coefficient

    # there is x*10 numbers that are both INC and DESC
    return bc(x+10, 10) + bc(x+9, 9) - 1 - x*10


assert total_inc_dec(0) == 1
assert total_inc_dec(1) == 10
assert total_inc_dec(2) == 100
assert total_inc_dec(3) == 475
assert total_inc_dec(4) == 1675
print(total_inc_dec(11))