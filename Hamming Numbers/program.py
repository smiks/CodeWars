from heapq import merge
from itertools import tee
 
def hamming_numbers():
    last = 1
    yield last
    a,b,c = tee(hamming_numbers(), 3)
    for n in merge((2*i for i in a), (3*i for i in b), (5*i for i in c)):
        if n != last:
            yield n
            last = n

def hamming(n):
    cache = dict()
    for e, h in enumerate(hamming_numbers()):
        cache[e+1] = h
        if e+1 == n:
            break
    return cache


c = hamming(5000)

print(c)

