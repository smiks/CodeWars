__author__ = 'Sandi'

def test(a, b, m):
    if a != b:
        print(m)


def f(n, m):
    m2 = m-1
    t = (m2*(m2+1))//2
    d1 = n/m
    d2 = n//m
    res = (d2)*t
    if d1 == d2:
        return res
    else:
        t2 = n-(d2*m)
        return res+((t2*(t2+1))//2)

# used for testing (using different approach)
def g(n, m):
    return sum(i%m for i in range(1, n+1))

assert f(10, 5) == 20

assert f(20, 20) == 190

assert f(15, 10) == 60

assert f(30, 15) == g(30, 15)

test(f(33, 15), g(33, 15), "Should be "+str(g(33,15)))