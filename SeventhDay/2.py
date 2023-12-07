def checkFullHouse(e, j, maxVal):
    if j == 0:
        if maxVal == 3 and 2 in e:
            return True
    if j == 1:
        if e.count(2) == 2:
            return True
    return False

def checkTwoPair(e, j, maxVal):
    if j == 0:
        if e.count(2) == 2:
            return True
    if j == 1:
        if maxVal == 2:
            return True
    return False


def findHandType(matches):
    j = 0
    if 'J' in matches:
        j = matches['J']
        del matches['J']
    e = list(matches.values())
    if j == 5:
        return 'five'
    maxVal = max(e)
    if maxVal + j == 5:
        return 'five'
    if maxVal + j == 4:
        return 'four'
    if checkFullHouse(e, j, maxVal):
        return 'fullHouse'
    if maxVal + j == 3:
        return 'three'
    if checkTwoPair(e, j, maxVal):
        return 'twoPair'
    if maxVal + j == 2:
        return 'pair'
    return 'hCard'

def easySortFormat(e):
    splited = e.split(' ')
    CARD = splited[0].lower().replace('a', 'm').replace('j', 'a').replace('k', 'l').replace('q', 'k').replace('t', 'j').replace('9', 'i').replace('8', 'h').replace('7', 'g').replace('6', 'f').replace('5', 'e').replace('4', 'd').replace('3', 'c').replace('2', 'b')
    BID = int(splited[1])
    return(CARD, BID)

def getHandTypes():
    handTypes = {
        'hCard': [],
        'pair': [],
        'twoPair': [],
        'three': [],
        'fullHouse': [],
        'four': [],
        'five': []
    }
    for e in INPUT:
        matches = {}
        for x in e.split(' ')[0]:
            if x in matches:
                matches[x] += 1
            else:
                matches[x] = 1
        type = findHandType(matches)
        handTypes[type].append(easySortFormat(e))
    return handTypes

def sortByStrongest(hands):
    toRet = []
    for hand in hands:
        sHand = sorted(hands[hand], key=lambda x: x[0])
        for e in sHand:
            toRet.append(e[1])
    return toRet

def getTotalWinnings(s_hands):
    toRet = 0
    for i,e in enumerate(s_hands):
        toRet += (i+1)*e
    return toRet

def main():
    HANDS = getHandTypes()
    S_HANDS = sortByStrongest(HANDS)
    res = getTotalWinnings(S_HANDS)
    print(res)

if __name__ == "__main__":
    INPUT = [
        '32T3K 765',
        'T55J5 684',
        'KK677 28',
        'KTJJT 220',
        'QQQJA 483'
    ]

    # with open('./input.txt') as t:
    #     INPUT = t.read().splitlines()

    main()