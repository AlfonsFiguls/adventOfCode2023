import re

def getNumsPos(e):
    return [m.span() for m in re.finditer(r"[\d]+", e)]

def getSymbols(e):
    return [m.start() for m in re.finditer(r"[*]", e)]

def checkNums(nums, n, i, INPUT):
    toRet = []
    for x in nums:
        if any(x in [n-1, n, n+1] for x in range(x[0],x[1])):
            val = int(INPUT[i][x[0]:x[1]])
            toRet.append(val)
    return toRet

def checkAdjacent(n, e, i, INPUT):
    adjacents = []
    
    # Current line
    numsPos = getNumsPos(e)
    if numsPos:
        toAdd = checkNums(numsPos, n, i, INPUT)
        if toAdd:
            adjacents += toAdd
        
    # Line above
    if i > 0:
        numsPos = getNumsPos(INPUT[i-1])
        if numsPos:
            toAdd = checkNums(numsPos, n, i-1, INPUT)
            if toAdd:
                adjacents += toAdd
    
    # Line below
    if i < len(INPUT)-1:
        numsPos = getNumsPos(INPUT[i+1])
        if numsPos:
            toAdd = checkNums(numsPos, n, i+1, INPUT)
            if toAdd:
                adjacents += toAdd

    if len(adjacents) == 2:
        return adjacents[0] * adjacents[1]
    else:   
        return 0

def sumGearRatios(INPUT):
    toRet = 0
    for i,e in enumerate(INPUT):
        symbols = getSymbols(e)
        for n in symbols:
            toAdd = checkAdjacent(n, e, i, INPUT)
            toRet += toAdd
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

    res = sumGearRatios(INPUT)
    print(res)