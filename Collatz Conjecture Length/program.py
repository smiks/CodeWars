def collatz(n, c=1):
    if n == 1: return c
    elif n%2: return collatz(3*n+1, c+1)
    else: return collatz(n/2, c+1)