import re
from collections import defaultdict
from collections import OrderedDict


""" I know, code is ugly. I was too lazy to refactor it :P """
def simplify(poly):
    """ find parts """
    leng = len(poly)
    parts = []
    signs = []
    lastS = 0
    for i in range(leng):
        """ check if first character is sign """
        if i == 0 and poly[0] == "-":
            fSignPos = 0
            signs.append(0)
        else:
            pf = poly.find("+", i)
            mf = poly.find("-", i)
            if pf == -1:
                fSignPos = mf
            elif mf == -1:
                fSignPos = pf
            else:
                fSignPos = min(mf, pf)

        if fSignPos != -1:
            part = poly[lastS:fSignPos].strip("+").strip("-")
            if part == "":
                continue
            signs.append(fSignPos)
            lastS = fSignPos
            i = fSignPos+1
            parts.append(part)

        else:  # we are at the last part
            part = poly[i:]
            parts.append(part)
            break

    """ sort parts """

    parts = list(map(lambda x: ''.join(sorted(x)), parts))
    """ initialize parameters for each part """
    dc = defaultdict(int)

    for e, p in enumerate(parts):
        """ get sign """
        if e == 0 and signs[0] == 0:
            sign = "-"
        elif e > 0 and e <= len(signs) and len(signs) < len(parts):
            sign = poly[signs[e-1]]
        elif e > 0 and e <= len(signs) and len(signs) == len(parts):
            sign = poly[signs[e]]
        else:
            sign = None

        pattern = "[0-9]+"
        m = re.search(pattern, p)
        if m is not None:
            n = m.group(0)
            pattern = "[a-z]+"
            m = re.search(pattern, p)
            x = m.group()
            if sign is not None:
                if sign == "+":
                    dc[x] += int(n)
                else:
                    dc[x] -= int(n)
            else:
                dc[x] += int(n)
        else:
            pattern = "[a-z]+"
            m = re.search(pattern, p)
            x = m.group()
            if sign is not None:
                if sign == "+":
                    dc[x] += 1
                else:
                    dc[x] -= 1
            else:
                dc[x] += 1


    """ re-make polynom """
    srt = sorted(dc.items(), key=lambda x: (len(x[0]), x ) )
    odc = OrderedDict(srt)
    new_poly = []
    for k, v in odc.items():
        if v == 0:
            continue
        elif v == 1:
            tmp = "+{0}" . format(k)
        elif v == -1:
            tmp = "-{0}" . format(k)
        elif v > 1:
            tmp = "+{0}{1}" . format(v, k)
        else:
            tmp = "+{0}{1}" . format(v, k)
        new_poly.append(tmp)

    polynom = ''.join(new_poly).strip("+").replace("+-", "-")

    #print("{0} -> {1}" . format(poly, polynom))
    return (polynom)






polys = [
    "-xyz+3zxy",
    "2xy+yx",
    "ax+bc-df+gg",
    "2xy-yx",
    "3xy+4bc-5yx-3cb+3bc",
    "-a+5ab+3a-c-2a"
]

for p in polys:
    simplify(p)


tests = {
    "dc+dcba": "cd+abcd",
    "2xy-yx": "xy",
    "-a+5ab+3a-c-2a": "-c+5ab",
    "a+ca-ab": "a-ab+ac",
    "-8fk+5kv-4yk+7kf-qk+yqv-3vqy+4ky+4kf+yvqkf": "3fk-kq+5kv-2qvy+fkqvy"
}

for inp, corr in tests.items():
    out = simplify(inp)
    print("INPUT: {0}, RESULT: {1} [{2}] " . format(inp, out, out == corr))