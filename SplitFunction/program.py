__author__ = 'Sandi'
def my_very_own_split(string, delimeter = None):
    if len(delimeter) == 1:
        tmp = ""
        for c in string:
            if c != delimeter:
                tmp += c
            else:
                yield tmp
                tmp = ""
        yield tmp

    else:
        dl = len(delimeter)
        tmp = string[0:dl-1]
        for i in range(0, len(string)-dl):
            p = string[i:i+dl]
            #print(p, end=" ")
            if p != delimeter:
                tmp += p[dl-1:]
            else:
                yield tmp[:-dl+1]
                tmp = ""
        yield tmp+string[-1]

s, d = 'abc,def,ghi', ','
#print(list(my_very_own_split(s, d)), s.split(d))
assert list(my_very_own_split(s, d)) == s.split(d)

s, d = ('abc,#def#,ghi,#jkl', ',#')
#print(list(my_very_own_split(s, d)), s.split(d))
assert list(my_very_own_split(s, d)) == s.split(d)

s, d = ('abc,##def#,ghi,##jkl', ',##')
#print(list(my_very_own_split(s, d)), s.split(d))
assert list(my_very_own_split(s, d)) == s.split(d)