__author__ = 'Sandi'
def doTheWork(money, coins, cs):
    if money == 0:
        return 1
    if money < 0:
        return 0
    if cs < 1 and money > 0:
        return 0
    return doTheWork(money, coins, cs - 1) + doTheWork(money-coins[cs-1], coins, cs)

def exp_sum(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n < 4:
        return n

    coins = [i for i in range(1,n+1)]
    return doTheWork(coins, len(coins), n)


# dynamic

# Dynamic Programming Python implementation of Coin Change problem
def doTheWork(S, m, n):
    # We need n+1 rows as the table is consturcted in bottom up
    # manner using the base case 0 value case (n = 0)
    table = [[0 for x in range(m)] for x in range(n+1)]

    # Fill the enteries for 0 value case (n = 0)
    for i in range(m):
        table[0][i] = 1

    # Fill rest of the table enteries in bottom up manner
    for i in range(1, n+1):
        for j in range(m):
            # Count of solutions including S[j]
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0

            # Count of solutions excluding S[j]
            y = table[i][j-1] if j >= 1 else 0

            # total count
            table[i][j] = x + y

    return table[n][m-1]

# Driver program to test above function
arr = [1, 2, 3]
m = len(arr)
n = 4
print(count(arr, m, n))