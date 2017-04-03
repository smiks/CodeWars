__author__ = 'Sandi'
import base64

def to_base_64(string):
    return base64.b64encode(string.encode("utf-8")).decode("utf-8").strip("=")

def from_base_64(string):
    string += "=="
    return base64.b64decode(string.encode("utf-8")).decode("utf-8")



s = "ScS6 nM:"
result = to_base_64(s)
print(result)
assert result == "U2NTNiBuTTo"

s = "d2hSS0JFY213WVZpNTIzUTEqUDc7O2tqOmlpQ2Q"
result = from_base_64(s)
print(result)
assert result == "whRKBEcmwYVi523Q1*P7;;kj:iiCd"