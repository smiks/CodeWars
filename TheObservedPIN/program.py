__author__ = 'Sandi'

from itertools import *

def get_pins2(observed):
    m = {0: [0, 8], 1: [1, 2, 4], 2: [1, 2, 3, 5], 3: [2, 3, 6],
         4: [1, 4, 5, 7], 5: [2, 4, 5, 6, 8], 6: [3, 5, 6, 9],
         7: [4, 7, 8], 8: [0, 5, 7, 8, 9], 9: [6, 8, 9]}

    mix = [m[int(c)] for c in observed]

    s = set()
    for p in product(*mix):
        s.add(''.join(map(str, p)))

    return list(s)


def test(a, b, m):
    if sorted(a) != sorted(b):
        print(m)



get_pins2("369")


#res = get_pins("8")
#test(res, ['5','7','8','9','0'], "Testing 8")

#res = get_pins("11")
#print(res)
#test(res, ["11", "22", "44", "12", "21", "14", "41", "24", "42"], "Testing 11 is wrong")


#res = get_pins("36")
#correct = ["33", "66", "26", "35", "39", "23", "29", "25", "36", "65"]
#print(res)


#res = get_pins("369")
#correct = ["339","366","399","658","636","258","268","669","668","266","369",
#           "398","256","296","259","368","638","396","238","356","659","639",
#           "666","359","336","299","338","696","269","358","656","698","699",
#            "298","236","239"]
"""
print()
print(sorted(res))
print(sorted(correct))
print(len(res))
print(len(correct))
test(res, correct, "Testing 369 is wrong")
"""