__author__ = 'Sandi'
def solution(string, markers):
    if len(string) == 0:
        return string
    newMarkers = []
    for m in markers:
        if m == "\xc2\xa7":
            newMarkers.append("§")
        else:
            newMarkers.append(m)
    markers = newMarkers
    lines = string.strip().split("\n")
    newText = []
    for l in lines:
        poss = []
        for m in markers:
            pos = l.find(m)
            #print("pos of ", m, " is ", pos)
            if pos != -1:
                poss.append(pos)
        if len(poss) > 0:
            text = l[:min(poss)]
        else:
            text = l
        newText.append(text.strip(" "))

    if string[0] == '\n':
        return "\n"
    return '\n'.join(newText)

#res = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
#print(res)

#res = solution("Â§", ['#', '\xc2\xa7'])
res = solution("\n§", ["#", "§"])
print(res)