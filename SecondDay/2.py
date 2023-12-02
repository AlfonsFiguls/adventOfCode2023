import re

def findPower(e):
    redVals = re.findall(r"([\d]+) red", e)
    greenVals = re.findall(r"([\d]+) green", e)
    blueVals = re.findall(r"([\d]+) blue", e)
    return max(list(map(int, redVals))) * max(list(map(int, greenVals))) * max(list(map(int, blueVals)))

def sumPower(inp):
    totalPower = 0
    for e in inp:
        power = findPower(e.split(':')[1])
        totalPower += power
    return totalPower


if __name__ == "__main__":
    RED = 12
    GREEN = 13
    BLUE = 14

    # INPUT = [
    #     'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    #     'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    #     'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    #     'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    #     'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
    # ]

    with open('./input.txt') as t:
        INPUT = t.readlines()

    res = sumPower(INPUT)
    print(res)