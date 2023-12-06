import re
import numpy as np

def getInitialMaps(e):
    maps =  [m.group(1).strip() for m in re.finditer(r"^([\d \n]+)$", e, re.MULTILINE)]
    return [x.split('\n') for x in maps]

def checkValInMap(map, val):
    for e in map:
        e = e.split(' ')
        DEST = int(e[0])
        SRC = int(e[1])
        RANGE = int(e[2])
        if val in range(DEST, DEST+RANGE):
            return SRC + val-DEST        
    return False

def checkExistSeed(SEEDS, val):
    for e in SEEDS:
        if val in e:
            return True
    return False

def reverseFind(MAPS, SEEDS):
    found = False
    location = 0
    while not found:
        val = location
        for map in reversed(MAPS):
            valInMap = checkValInMap(map, val)
            if valInMap:
                val = valInMap
        if checkExistSeed(SEEDS, val):
            found = True
        else:
            location += 1
    return location

def getSeeds(preSeeds):
    toRet = []
    x = 0
    while x<len(preSeeds):
        toRet.append(range(preSeeds[x], preSeeds[x] + preSeeds[x + 1]))
        x += 2
    return toRet

def main():
    MAPS = getInitialMaps(INPUT)
    PRE_SEEDS = [int(m.group()) for m in re.finditer(r"[\d]+", INPUT.split('\n')[0])]
    SEEDS = getSeeds(PRE_SEEDS)
    MIN_LOC = reverseFind(MAPS, SEEDS)
    print(MIN_LOC)

if __name__ == "__main__":

    INPUT = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

    # with open('./input.txt') as t:
    #     INPUT = t.read()

    main()
