import re

def getNumsPos(e):
    return [m.span() for m in re.finditer(r"[\d]+", e)]

def getSymbolsPos(e):
    return [m.start() for m in re.finditer(r"[^\d.]", e)]

def checkSymbols(symbols, n):
    for x in symbols:
        if x in range(n[0]-1, n[1]+1):
            return True
    return False

def checkAdjacent(n, e, i, INPUT):
    # Current line
    symbols = getSymbolsPos(e)
    if symbols:
        if checkSymbols(symbols, n):
            return True
    
    # Line above
    if i > 0:
        symbols = getSymbolsPos(INPUT[i-1])
        if symbols:
            if checkSymbols(symbols, n):
                return True
    
    # Line below
    if i < len(INPUT)-1:
        symbols = getSymbolsPos(INPUT[i+1])
        if symbols:
            if checkSymbols(symbols, n):
                return True
    return False

def sumAdjacent(INPUT):
    toRet = 0
    for i,e in enumerate(INPUT):
        numsPos = getNumsPos(e)
        for n in numsPos:
            if checkAdjacent(n, e, i, INPUT):
                toRet += int(e[n[0]:n[1]])
    return toRet


if __name__ == "__main__":
    INPUT = [
        '467..114..',
        '...*......',
        '..35..633.',
        '......#...',
        '617*......',
        '.....+.58.',
        '..592.....',
        '......755.',
        '...$.*....',
        '.664.598..'
    ]

    # with open('./input.txt') as t:
    #     INPUT = t.read().splitlines()

    res = sumAdjacent(INPUT)
    print(res)