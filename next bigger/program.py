def pi(s, pos):
    return int(s[pos])

def sameNumbers(a, b):
    return sorted(str(a)) == sorted(str(b))

def is_sorted(s, order="ASC"):
    prev = s[0]
    for i in s:
        if i < prev and order == "ASC":
            return False
        elif i > prev and order == "DESC":
            return False
        prev = i
    return True

def next_bigger(n):
    from collections import Counter
    s = str(n)
    """ check if all numbers are the same """
    cs = Counter(s)
    if len(s) == cs[s[0]]:
        return -1
    if is_sorted(s, order="DESC"):
        return -1
    if len(s) == 2 and is_sorted(s):
        return int(''.join(reversed(s)))
    sn = sorted(str(n))

    if len(s) < 15:
        for i in range(n+1, n*10):
            if sorted(str(i)) == sn:
                return i

    prev = pi(s, 0)
    changePos = -1
    change = -1
    smallPos = -1
    small = 10
    for e, c in enumerate(s):
        c = int(c)
        if c < prev and changePos == -1:
            changePos = e
            change = c
        if c > change and c < small and changePos != -1:
            small = c
            smallPos = e

        prev = c

    left = s[:changePos]
    right = ''.join(sorted(s[changePos:smallPos]+s[smallPos+1:]))
    ret = int(left+s[smallPos]+right)

    return ret

"""
assert next_bigger(111) == -1
assert next_bigger(12) == 21
assert next_bigger(513) == 531
assert next_bigger(2017) == 2071
assert next_bigger(414) == 441
assert next_bigger(144) == 414
assert next_bigger(123456784987654321) == 123456785123446789
assert next_bigger(123456789) == 123456798
"""
assert next_bigger(1234567890) == 1234567908
"""
#res = next_bigger(123456789)
#print(res)
"""