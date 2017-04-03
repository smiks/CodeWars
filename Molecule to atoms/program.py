from CodeWarsTests import *

from collections import defaultdict
from string import (ascii_lowercase as alow,
ascii_uppercase as aupp)

def parse_molecule (formula):
    atoms = defaultdict(int)
    nums = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

    def rec(f):
        stack_n = []
        stack_a = []
        f  = f[::-1]
        tmp = []
        pn = ""
        pa = ""
        p1 = ["(", "[", "{"]
        p2 = [")", "]", "}"]
        multi = 1
        for c in f:
            # parse number and put in stack_n
            # if bracket put atoms on stack_a
            # atoms on same contigous level are in a list tmp
            if c in alow:
                pa = c

            if c in aupp:
                pa = c+pa
                if pn == "":
                    pn = "1"
                atoms[pa] += int(multi*int(pn))
                pn = ""
                pa = ""

            if c in nums:
                pn += c

            if c in p2:
                pn = pn[::-1]
                if pn == "":
                    pn = "1"
                pn = int(pn)
                stack_n.append(pn)
                multi *= pn
                pn = ""

            if c in p1:
                multi /= stack_n.pop()

        return atoms

    def lp(f):
        f = f+"X"
        pa = ""
        pn = ""
        for e, c in enumerate(f):
            if c in aupp:
                if pn != "":
                    atoms[pa] += int(pn)
                elif pn == "" and pa in aupp and e > 0:
                    atoms[pa] += 1
                elif len(pa) > 1:
                    atoms[pa] += 1
                pa = c
                pn = ""
            elif c in alow:
                pa = pa+c
                pn = ""
            elif c in nums:
                pn = pn+c

        return atoms


    ps = ["[", "(", "{"]
    pe = False
    for p in ps:
        if p in formula:
            pe = True

    return rec(formula) if pe else lp(formula)

def equals_atomically (obj1, obj2):
    if len(obj1) != len(obj2):
        return False
    for k in obj1:
        if obj1[k] != obj2[k]:
            return False
    return True

Test.expect(equals_atomically(parse_molecule("H2O"), {'H': 2, 'O' : 1}), "Should parse water")
Test.expect(equals_atomically(parse_molecule("C6H12O6"), {'C': 6, 'H': 12, 'O' : 6}), "Should parse glucose")
Test.expect(equals_atomically(parse_molecule("NaCl"), {'Na': 1, 'Cl': 1}), "Should parse salt")
Test.expect(equals_atomically(parse_molecule("Ca2Cl"), {'Ca': 2, 'Cl': 1}), "Should parse Ca2Cl")
Test.expect(equals_atomically(parse_molecule("Ca2Cl2"), {'Ca': 2, 'Cl': 2}), "Should parse Ca2Cl2")
Test.expect(equals_atomically(parse_molecule("CaCO3"), {'Ca': 1, 'C': 1, 'O':3}), "Should parse calcium carbonate")

Test.expect(equals_atomically(parse_molecule("Mg(OH)2"), {'Mg': 1, 'O' : 2, 'H': 2}), "Should parse magnesium hydroxide: Mg(OH)2")
Test.expect(equals_atomically(parse_molecule("Mg(OH)2(OH)12"), {'Mg': 1, 'O' : 14, 'H': 14}), "Should parse Mg(OH)2(OH)12")
Test.expect(equals_atomically(parse_molecule("K4[ON(SO3)2]2"), {'K': 4,  'O': 14,  'N': 2,  'S': 4}), "Should parse Fremy's salt: K4[ON(SO3)2]2")
