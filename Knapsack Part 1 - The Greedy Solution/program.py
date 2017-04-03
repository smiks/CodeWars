from CodeWarsTests import *

def knapsack(capacity, items):
    from copy import deepcopy
    orig = deepcopy(items)
    ret = {i:0 for i in items}
    items = [(i[1]/i[0],i) for i in items]
    items.sort()
    cc = 0
    while cc < capacity:
        if len(items) == 0:
            break
        item = items.pop()[1]
        w = item[0]
        while cc+w <= capacity:
            cc += w
            ret[item] += 1
    return [ret[i] for i in orig]


Test.describe('One item')
Test.assert_equals(knapsack(100, ((1, 1),)), [100])
Test.assert_equals(knapsack(100, ((100, 1),)), [1])


Test.describe('Two items')
Test.assert_equals(knapsack(100, ((1, 1),
                                  (3, 4))), [1, 33])
Test.assert_equals(knapsack(100, ((60, 80),
                                  (50, 50))), [1, 0])


Test.describe('Three items')
Test.assert_equals(knapsack(100, ((10, 10),(30, 40), (56, 78))), [1, 1, 1])

Test.assert_equals(knapsack(100, ((11.2,  7.4),(25.6, 17.8),(51.0, 41.2),(23.9, 15.6),(27.8, 19.0))), [2, 1, 1, 0, 0])
