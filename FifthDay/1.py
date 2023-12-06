import re

def getInitialMaps(e):
    maps =  [m.group(1).strip() for m in re.finditer(r"^([\d \n]+)$", e, re.MULTILINE)]
    return [x.split('\n') for x in maps]

def checkValInMap(map, val):
    for e in map:
        e = e.split(' ')
        DEST = int(e[0])
        SRC = int(e[1])
        RANGE = int(e[2])
        if val in range(SRC, SRC+RANGE):
            return DEST + val-SRC        
    return False

def findLocations(maps, seeds):
    locations = []
    for seed in seeds:
        val = seed
        for map in maps:
            valInMap = checkValInMap(map, val)
            if valInMap:
                val = valInMap
        locations.append(val)
    return locations

def main():
    MAPS = getInitialMaps(INPUT)
    SEEDS = [int(m.group()) for m in re.finditer(r"[\d]+", INPUT.split('\n')[0])]
    LOCATIONS = findLocations(MAPS, SEEDS)
    print(min(LOCATIONS))

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
