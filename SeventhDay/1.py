def findHandType(e):
    maxVal = max(e)
    if maxVal == 5:
        return 'five'
    if maxVal == 4:
        return 'four'
    if maxVal == 3 and 2 in e:
        return 'fullHouse'
    if maxVal == 3:
        return 'three'
    if e.count(2) == 2:
        return 'twoPair'
    if maxVal == 2:
        return 'pair'
    return 'hCard'

def easySortFormat(e):
    splited = e.split(' ')
    CARD = splited[0].lower().replace('a', 'm').replace('k', 'l').replace('q', 'k').replace('t', 'i').replace('9', 'h').replace('8', 'g').replace('7', 'f').replace('6', 'e').replace('5', 'd').replace('4', 'c').replace('3', 'b').replace('2', 'a')
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
        type = findHandType(list(matches.values()))
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