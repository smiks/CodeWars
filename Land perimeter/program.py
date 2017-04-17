def land_perimeter(arr):
    # each X brings 4 units
    # each 2 adjacent Xs subtract 2 unit
    Xs = sum(4 if c == "X" else 0 for r in arr for c in r)

    for r in arr:
        for i in range(len(r)-1):
            a,b = r[i], r[i+1]
            if a == b and b == "X":
                Xs -= 2
                
    for c in zip(*arr):
        for i in range(len(c)-1):
            a,b = c[i], c[i+1]
            if a == b and b == "X":
                Xs -= 2                

    return "Total land perimeter: {0}" . format(Xs)