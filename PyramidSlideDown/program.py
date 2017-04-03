__author__ = 'Sandi'
def longest_slide_down(p):
    rlen = len(p)
    # through rows
    for i in range(rlen-1, 0, -1):
        # through cols
        for j in range(0, len(p[i])-1):
            left = p[i][j]
            right = p[i][j+1]
            parent = p[i-1][j]
            p[i-1][j] = max(left+parent, right+parent)

    return p[0][0]

longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]])