def find_word(board, word):
    from collections import defaultdict as dd

    x = [-1, -1, -1, 0, 0, 1, 1, 1]
    y = [-1, 0, 1, -1, 1, -1, 0, 1]
    taken = dd(bool)


    def search(grid, posX, posY, currIndex, word, taken):
        if currIndex == len(word):
            return True

        toLook = word[currIndex]

        """ check neighbours """
        for d in range(8):
            rd = posX+x[d]
            cd = posY+y[d]

            if rd < 0 or rd >= len(grid) or cd < 0 or cd >= len(grid[0]):
                continue

            if not taken[(rd,cd)] and grid[rd][cd] == toLook:
                old_taken = taken
                taken[(rd,cd)] = True
                if search(grid, rd, cd, currIndex+1, word, taken):
                    return True
                taken = old_taken

    """ find first occurrence """
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == word[0]:
                taken[(row, col)] = True
                if len(word) == 1:
                    return True

                if search(board, row, col, 1, word, taken):
                    return True
                else:
                    taken = dd(bool)

    return False