__author__ = 'Sandi'
class RomanNumerals():
    def __init__(self):
        self.romanNumerals = [('M', 1000),
                         ('CM', 900),
                         ('D', 500),
                         ('CD', 400),
                         ('C', 100),
                         ('XC', 90),
                         ('L', 50),
                         ('XL', 40),
                         ('X', 10),
                         ('IX', 9),
                         ('V', 5),
                         ('IV', 4),
                         ('I', 1)]
    @staticmethod
    def to_roman(n):
        romanNumerals = [('M', 1000),
                                 ('CM', 900),
                                 ('D', 500),
                                 ('CD', 400),
                                 ('C', 100),
                                 ('XC', 90),
                                 ('L', 50),
                                 ('XL', 40),
                                 ('X', 10),
                                 ('IX', 9),
                                 ('V', 5),
                                 ('IV', 4),
                                 ('I', 1)]
        ret = ""
        for numeral, i in romanNumerals:
            while n >= i:
                ret += numeral
                n -= i
        return ret

    @staticmethod
    def from_roman(s):
        romanNumerals = [('M', 1000),
                                 ('CM', 900),
                                 ('D', 500),
                                 ('CD', 400),
                                 ('C', 100),
                                 ('XC', 90),
                                 ('L', 50),
                                 ('XL', 40),
                                 ('X', 10),
                                 ('IX', 9),
                                 ('V', 5),
                                 ('IV', 4),
                                 ('I', 1)]
        ret = 0
        i = 0
        """ iterate through numerals/pairs """
        for numeral, ar in romanNumerals:
            while s[i:i+len(numeral)] == numeral:
                ret += ar
                i += len(numeral)
        return ret


print(RomanNumerals.to_roman(1000))
print(RomanNumerals.from_roman('M'))