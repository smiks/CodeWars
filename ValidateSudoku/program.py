__author__ = 'Sandi'
class Sudoku(object):
    def __init__(self, sudo):
        self.sudo = sudo

    def check(self, row):
        for v in row.values():
            if v != 1:
                return False
        return True

    def is_valid(self):
        su = self.sudo  # less typing in the future

        """ check dimensions """
        shouldBe = len(su)
        for row in su:
            if len(row) != shouldBe:
                return False

        """ assign allowed values """
        allowedValues = {i for i in range(1,shouldBe+1)}

        """ check rows """
        nums = [{i:0 for i in range(1, shouldBe+1)}for _ in range(shouldBe)]
        for e, row in enumerate(su):
            for el in row:
                if not isinstance(el, int) or el not in allowedValues:
                    return False
                nums[e][el] += 1

            if not self.check(nums[e]):
                return False

        """ check columns """
        nums = [{i:0 for i in range(1, shouldBe+1)}for _ in range(shouldBe)]
        for e, col in enumerate(zip(*su)):
            for el in col:
                if isinstance(el, bool) or not isinstance(el, int) or el not in allowedValues:
                    return False
                nums[e][el] += 1

            if not self.check(nums[e]):
                return False


        """ check quadrants """
        qsize = int(shouldBe**0.5)

        """ iterate through quadrants """
        for i in range(qsize):
            for j in range(qsize):
                toCheck = {i:0 for i in range(1, shouldBe+1)}

                """ iterate through single quadrant """
                for row in range(i*qsize, (i+1)*qsize):
                    for col in range(j*qsize, (j+1)*qsize):
                        tmp = su[row][col]
                        toCheck[tmp] += 1

                if not self.check(toCheck):
                    return False

        return True

goodSudoku1 = Sudoku([
  [7,8,4, 1,5,9, 3,2,6],
  [5,3,9, 6,7,2, 8,4,1],
  [6,1,2, 4,3,8, 7,5,9],

  [9,2,8, 7,1,5, 4,6,3],
  [3,5,7, 8,4,6, 1,9,2],
  [4,6,1, 9,2,3, 5,8,7],

  [8,7,6, 3,9,4, 2,1,5],
  [2,4,3, 5,6,1, 9,7,8],
  [1,9,5, 2,8,7, 6,3,4]
])

goodSudoku2 = Sudoku([
  [1,4, 2,3],
  [3,2, 4,1],

  [4,1, 3,2],
  [2,3, 1,4]
])
badSudoku2 = Sudoku([
  [1,2,3,4,5],
  [1,2,3,4],
  [1,2,3,4],
  [1]
])

badSudoku3 = Sudoku([[True]])
badSudoku4 = Sudoku([[1, 4, 4, 3, 'a'], [3, 2, 4, 1], [4, 1, 3, 3], [2, 0, 1, 4], ['', False, None, '4']])
badSudoku5 = Sudoku([[1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 1, 5, 6, 4, 8, 9, 7], [3, 1, 2, 6, 4, 5, 9, 7, 8], [4, 5, 6, 7, 8, 9, 1, 2, 3], [5, 6, 4, 8, 9, 7, 2, 3, 1], [6, 4, 5, 9, 7, 8, 3, 1, 2], [7, 8, 9, 1, 2, 3, 4, 5, 6], [8, 9, 7, 2, 3, 1, 5, 6, 4], [9, 7, 8, 3, 1, 2, 6, 4, 5]])


""" valid sudokus """
assert goodSudoku1.is_valid()
assert goodSudoku2.is_valid()

""" invalid sudokus """
assert not badSudoku2.is_valid()
assert not badSudoku3.is_valid()
assert not badSudoku4.is_valid()
assert not badSudoku5.is_valid()