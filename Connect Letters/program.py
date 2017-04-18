def calc(l, r, s):
    # prefill memo
    memo = [[-1 for __ in range(r+1)] for _ in range(r+1)]
    def calc2(l, r):
        mres = memo[l][r]
        if mres != -1:
            return mres
        if l >= r:
            return 0

        res = calc2(l+1, r)
        a = s[l]
        for k in range(l+1,r):
            b = s[k]
            if a == "A" and b == "B" or \
                a == "B" and b == "A" or \
                a == "X" and b == "Y" or \
                a == "Y" and b == "X":

                res = max(res, 1 + calc2(l+1, k) + calc2(k+1, r))

        if mres == -1:
            memo[l][r] = res

        return res

    return calc2(l, r)


def match(s):
    ls = len(s)
    if ls < 2:
        return 0

    # preprocess a string
    # check for adjacent
    pre_conn = 0
    depair = True
    mtch = ["AB", "BA", "XY", "YX"]
    while depair:
        depair = False
        for i in range(ls-2, -1, -1):
            subs = s[i:i+2]
            if subs in mtch:
                s = s[0:i]+s[i+2:]
                pre_conn += 1
                depair = True
                break

    if len(s) < 3:
        return pre_conn

    # check for edges
    edges = True
    while edges:
        edges = False
        if s[0] == "A" and s[-1] == "B":
            pre_conn += 1
            s = s[1:-1]
            edges = True
        if s[0] == "B" and s[-1] == "A":
            pre_conn += 1
            s = s[1:-1]
            edges = True
        if s[0] == "X" and s[-1] == "Y":
            pre_conn += 1
            s = s[1:-1]
            edges = True
        if s[0] == "Y" and s[-1] == "X":
            pre_conn += 1
            s = s[1:-1]
            edges = True

    res = calc(0, len(s), s)
    return res + pre_conn