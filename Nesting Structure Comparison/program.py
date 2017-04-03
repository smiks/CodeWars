from CodeWarsTests import *

def same_structure_as(original, other):
    def check(l, s):
        if isinstance(l, list):
            s += '['
            for a in l:
                s += check(a, s) if isinstance(a, list) else 'x'
            s += ']'
        return s
    return check(original, "") == check(other, "")




Test.assert_equals(same_structure_as([1,[1,1]],[2,[2,2]]), True, "[1,[1,1]] same as [2,[2,2]]")
Test.assert_equals(same_structure_as([1,[1,1]],[[2,2],2]), False, "[1,[1,1]] not same as [[2,2],2]")
Test.assert_equals(same_structure_as([1, [1, 1]], [2, [2]]), False, "[1,[1,1]] not same as [2,[2]]")
Test.assert_equals(same_structure_as([[[],[]]], [[1,1]]), False, "[[[],[]]] not same as [[1,1]]")
Test.assert_equals(same_structure_as([1,'[',']'], ['[',']',1]), True, "[1,'[',']'] same as ['[',']',1]")
