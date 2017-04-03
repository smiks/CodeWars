__author__ = 'Sandi'
from math import sqrt
class Primes:

    @staticmethod
    def is_prime(p):
        """
        Function checks if n is prime number or not.
        This function is used as wrapper for Miller-Rabin
        to maintain backwards compatibility.
        :param p: Number to be checked if prime or not.
        :return: Returns boolean, True if number is prime otherwise False.
        """
        try:
            int(p)
        except ValueError:
            return -1

        if p < 1e7:
            if p < 2:
                return False
            if p == 2:
                return True
            if p > 2 and p%2 == 0:
                return False
            upper_bound = int(sqrt(p)+1)
            for i in range(3, upper_bound, 2):
                if p%i == 0:
                    return False
            return True

        return Primes.Miller_Rabin(p)

    @staticmethod
    def Miller_Rabin(n, k = 100):
        from random import randrange
        """
        Tries if n is prime in k passes of Miller-Rabin primality test.
        :param n: Number to be checked if prime.
        :param k: Number of rounds of Miller-Rabin test.
        :return: Returns True if number is prime, else False
        """
        small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 34, 47,
                        53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
                        109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
                        173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
                        233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
                        293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
                        367, 373, 379, 383, 389, 397, 401, 409, 419, 419, 421,
                        431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487,
                        491, 499, 503, 509, 521, 523, 541]
        if n < 2:
            return False

        for p in small_primes:
            if n < p * p:
                return True
            if n % p == 0:
                return False

        # taking care of some multipliers
        if n > 7 and (n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0):
            return False

        r, s = 0, n - 1
        while s % 2 == 0:
            r += 1
            s //= 2

        for _ in range(k):
            a = randrange(2, n - 1)
            x = pow(a, s, n)
            if x == 1 or x == n - 1:
                continue

            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True


    @staticmethod
    def first(n):
        s = 2
        p = []
        while s < 1000000000:
            if len(p) == n:
                return p

            if Primes.is_prime(s):
                p.append(s)
            s += 1 if s%2 == 0 else 2

        return p[:n]


print(Primes.first(5))
assert Primes.first(5) == [2, 3, 5, 7, 11]

assert Primes.first(20)[-5:] == [53, 59, 61, 67, 71]