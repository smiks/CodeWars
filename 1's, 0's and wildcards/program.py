from itertools import product

def possibilities(param):
    cq = param.count("?")
    if cq == 0:
        return [param]
    param = param.replace("?", "{}")
    return [param.format(*perm) for perm in product(["1", "0"], repeat=cq)]


tests = {
    #'101?': ['1010', '1011'],
    '1?1?': ['1010', '1110', '1011', '1111']
}

for inp, res in tests.items():
    res = sorted(res)
    ou = sorted(possibilities(inp))
    print("{0}\t->\t{1}\t\t{2}" . format(inp, ou, res==ou))