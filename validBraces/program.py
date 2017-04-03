__author__ = 'Sandi'
def validBraces(string):
    obrackets = []
    obraces = []
    oparanthesis = []

    cbrackets = []
    cbraces = []
    cparanthesis = []

    for c in string:
        if c == ")" and len(oparanthesis) == 0:
          return False
        if c == "]" and len(obrackets) == 0:
          return False
        if c == "}" and len(obraces) == 0:
          return False

        if c == ")":
            oparanthesis.pop()
        if c == "(":
            if len(obrackets) != 0 or len(obraces) != 0:
                return False
            oparanthesis.append("(")

        if c == "]":
            obrackets.pop()
        if c == "[":
            obrackets.append("[")

        if c == "}":
            obraces.pop()
        if c == "{":
            obraces.append("{")

    if len(obraces) != 0 or len(obrackets) != 0 or len(oparanthesis) != 0:
        return False

    return True



assert validBraces( "(}" ) == False
assert validBraces( "[(])" ) == False
assert validBraces( "(){}[]" ) == True
assert validBraces( "([{}])" ) == True