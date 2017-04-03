__author__ = 'Sandi'
def pick_peaks(arr):
    if len(arr) == 0:
        return {"pos": [], "peaks": []}
    # remove first and last
    orig = arr[::]
    arr = arr[1:]
    prev = arr[0]
    pos = []
    peaks = []
    bottom = True
    for e, i in enumerate(arr):
        if i <= prev and bottom and e > 0:
            # check if bigger follows
            follows = False
            if i == prev:
                for p in range(e, len(arr)):
                    if arr[p] > i:
                        follows = True
                        break
                    if arr[p] < i:
                        break

            if prev < i or not follows:
                peaks.append(prev)
                pos.append(e)
                bottom = False
        if i > prev and not bottom:
            bottom = True
        prev = i

    """ check for weird edge """
    if len(pos) > 0:
        lastPos = pos[-1]
        lastPeak = peaks[-1]
        edge = True
        for p in range(lastPos, len(arr)):
            if arr[p] != lastPeak:
                edge = False

    if len(pos) > 0 and edge and lastPeak == orig[-1]:
        peaks.pop()
        pos.pop()

    if len(pos) > 0 and orig[-1] < arr[-1]:
        peaks.append(arr[-1])
        pos.append(len(arr))

    if len(pos) > 0 and orig[0] >= arr[0] and arr[0] == peaks[0]:
        peaks = peaks[1:]
        pos = pos[1:]

    return {"pos":pos, "peaks":peaks}


# test 1
#print(pick_peaks([1,2,3,6,4,1,2,3,2,1]))
assert pick_peaks([1,2,3,6,4,1,2,3,2,1]) == {"pos":[3,7], "peaks":[6,3]}

# test 2
#print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]))
assert pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]) == {"pos":[3,7,10], "peaks":[6,3,2]}

# test 3
#print(pick_peaks([2,1,3,1,2,2,2,2]))
assert pick_peaks([2,1,3,1,2,2,2,2]) == {"pos":[2], "peaks":[3]}

# test I
#         2              7           11       14                20
# 1,   2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4,    3
#print(pick_peaks([1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3]))
assert pick_peaks([1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3]) == {'pos': [2, 7, 14, 20], 'peaks': [5, 6, 5, 5]}

# test R I
#print(pick_peaks([-2, 15, -1, 17, 12, 13, 17, -5]))
assert pick_peaks([-2, 15, -1, 17, 12, 13, 17, -5]) == {'pos': [1, 3, 6], 'peaks': [15, 17, 17]}

# test R II
#print(pick_peaks([11, 4, 0, -3, -3, 3, 11, -5]))
assert pick_peaks([11, 4, 0, -3, -3, 3, 11, -5]) == {'pos': [6], 'peaks': [11]}

# test R III
#print(pick_peaks([16, 16, -3, 20, 19, 19, -5, -3, 4]))
assert pick_peaks([16, 16, -3, 20, 19, 19, -5, -3, 4]) == {'pos': [3], 'peaks': [20]}

# test X
#print(pick_peaks([0, -4, -3, 4, 4]))