def getLowerRange(TIME, DISTANCE):
    loop = True
    val = 0
    while loop:
        remainingTime = TIME - val
        if remainingTime * val > DISTANCE:
            loop = False
        else:
            val += 1
    return val

def getUpperRange(TIME, DISTANCE):
    loop = True
    val = TIME
    while loop:
        remainingTime = TIME - val
        if remainingTime * val > DISTANCE:
            loop = False
        else:
            val -= 1
    return val

def getWinningOptions(TIME, DISTANCE):
    LOWER = getLowerRange(TIME, DISTANCE)
    UPPER = getUpperRange(TIME, DISTANCE)
    return len(range(LOWER, UPPER+1))
            

def main():
    TIME = int(INPUT.split('\n')[0].replace('Time:', '').replace(' ', ''))
    DISTANCE = int(INPUT.split('\n')[1].replace('Distance:', '').replace(' ', ''))
    OPTIONS = getWinningOptions(TIME, DISTANCE)
    print(OPTIONS)

if __name__ == "__main__":
    INPUT = """Time:      7  15   30
    Distance:  9  40  200"""
    # with open('./input.txt') as t:
    #     INPUT = t.read()
    main()