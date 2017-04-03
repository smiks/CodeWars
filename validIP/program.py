__author__ = 'Sandi'
import re
def is_valid_IP(s):
    if len(s) < 6:
        return False
    ex = s.split(".")
    if len(ex) != 4:
        return False
    for p in ex:
        m = re.search(r"[0-9]+", p)
        if p.find(" ") != -1:
            return False
        if m is None:
            return False
        if len(p) > 1 and p[0] == "0" and p[1] != "0":
            return False
        if len(p) > 2 and p[0] == "0" and p[1] == "0" and p[2] != "0":
            return False
        if p == "000":
            return False
        try:
            p = int(p)
        except:
            return False
        if p < 0 or p > 255:
            return False
    return True





assert is_valid_IP('abc.def.ghi.jkl') == False
assert is_valid_IP('123.123.123.123') == True
assert is_valid_IP('123.456.789.0') == False
assert is_valid_IP('') == False
assert is_valid_IP('12.34.56') == False
assert is_valid_IP('123.045.067.089') == False
assert is_valid_IP('12.34.56 .1') == False
assert is_valid_IP("1.2.3.4Â ") == False
assert is_valid_IP("1.2.3.4Â ") == False
