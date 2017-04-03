__author__ = 'Sandi'
def check(row):
    for v in row.values():
        if v != 1:
            return False
    return True

def validSolution(board):
    su = board  # less typing in the future

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

        if not check(nums[e]):
            return False

    """ check columns """
    nums = [{i:0 for i in range(1, shouldBe+1)}for _ in range(shouldBe)]
    for e, col in enumerate(zip(*su)):
        for el in col:
            if isinstance(el, bool) or not isinstance(el, int) or el not in allowedValues:
                return False
            nums[e][el] += 1

        if not check(nums[e]):
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

            if not check(toCheck):
                return False

    return True