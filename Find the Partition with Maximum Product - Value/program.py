def find_part_max_prod(n):
    from functools import reduce
    mxpr = 0
    mxpa = []
    def partitions(n):
        if n == 0:
            yield []
            return
        for p in partitions(n - 1):
            yield [1] + p
            if p and (len(p) < 2 or p[1] > p[0]):
                yield [p[0] + 1] + p[1:]

    """ find max """
    parts = [sorted(p, key=lambda x: -x) for p in partitions(n)]
    for p in parts:
        mxpr = max(mxpr, reduce(lambda x,y: x*y, p))

    for p in parts:
        if reduce(lambda x,y: x*y, p) >= mxpr:
            mxpa.append(p)

    return [p for p in sorted(mxpa, key=lambda x: len(x) )] + [mxpr]