def no_repeat(string):
    from collections import defaultdict as dd
    d = dd(int)
    for i in string:
        d[i] += 1
    for i in string:
        if d[i] == 1:
            return i