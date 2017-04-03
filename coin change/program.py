__author__ = 'Sandi'

def doTheWork(money, coins, cs):
    if money == 0:
        return 1
    if money < 0:
        return 0
    if cs < 1 and money > 0:
        return 0
    return doTheWork(money, coins, cs - 1) + doTheWork(money-coins[cs-1], coins, cs)

def count_change(money, coins):
    return doTheWork(money, coins, len(coins))

assert count_change(4, [1,2]) == 3
assert count_change(10, [5,2,3]) == 4
assert count_change(11, [5,7]) == 0