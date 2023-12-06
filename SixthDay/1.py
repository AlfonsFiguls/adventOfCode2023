import re
from functools import reduce

def parseInpVals(e):
    return [int(m.group()) for m in re.finditer(r"[\d]+", e)]

def getWinningOptions(TIME, DISTANCE):
    options = []
    for i in range(len(TIME)):
        optionsInLoop = 0
        for t in range(TIME[i]):
            remainingTime = TIME[i] - t
            if remainingTime * t > DISTANCE[i]:
                optionsInLoop += 1
        options.append(optionsInLoop)
    return options
            

def main():
    TIME = parseInpVals(INPUT.split('\n')[0])
    DISTANCE = parseInpVals(INPUT.split('\n')[1])
    OPTIONS = getWinningOptions(TIME, DISTANCE)
    N_WAYS = reduce(lambda x, y: x * y, OPTIONS)
    print(N_WAYS)

if __name__ == "__main__":
    INPUT = """Time:      7  15   30
    Distance:  9  40  200"""
    # with open('./input.txt') as t:
    #     INPUT = t.read()
    main()