from functools import reduce
find_difference = lambda a,b: abs(reduce(lambda x, y:x*y, a) - reduce(lambda x, y:x*y, b))