import re

def isPossible(e):
    redVals = re.findall(r"([\d]+) red", e)
    if any(int(x) > RED for x in redVals):
        return False
    greenVals = re.findall(r"([\d]+) green", e)
    if any(int(x) > GREEN for x in greenVals):
        return False
    blueVals = re.findall(r"([\d]+) blue", e)
    if any(int(x) > BLUE for x in blueVals):
        return False
    return True

def countIDs(inp):
    toRet = 0
    for e in inp:
        splited = e.split(':')
        if isPossible(splited[1]):
            toRet += int(splited[0].split(' ')[1])
    return toRet


if __name__ == "__main__":
    RED = 12
    GREEN = 13
    BLUE = 14

    INPUT = [
        'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
        'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
        'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
        'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
        'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
    ]

    # with open('./input.txt') as t:
    #     INPUT = t.readlines()

    res = countIDs(INPUT)
    print(res)