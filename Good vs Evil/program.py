__author__ = 'Sandi'

def goodVsEvil(good, evil):
    g = [1, 2, 3, 3, 4, 10]
    e = [1, 2, 2, 2, 3, 5, 10]
    goodList = good.strip().split(" ")
    evilList = evil.strip().split(" ")
    gp = sum(g[en]*i for en, i in enumerate(map(int, goodList)))
    ep = sum(e[en]*i for en, i in enumerate(map(int, evilList)))
    if gp > ep:
        return "Battle Result: Good triumphs over Evil"
    if gp < ep:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"