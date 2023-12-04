import re
from functools import reduce

def returnNumList(e):
    return [m.group() for m in re.finditer(r"[\d]+", e)]

def returnNMatchingNums(nums, wNums):
    matches = 0
    for n in nums:
        if n in wNums:
            matches += 1
    return matches

def addCardsToCount(m, cardCount, i, times):
    i += 1
    for x in range(i,i+m):
        if x<len(cardCount):
            cardCount[x] += times
    return cardCount

def countPoints():
    cardCount = [1 for _ in range(len(INPUT))]
    for i,e in enumerate(INPUT):
        splited = e.split('|')
        wNums = returnNumList(splited[0].split(': ')[1])
        nums = returnNumList(splited[1])
        matches = returnNMatchingNums(nums, wNums)
        cardCount = addCardsToCount(matches, cardCount, i, cardCount[i])
    return reduce(lambda x, y: x + y, cardCount)

if __name__ == "__main__":
    INPUT = [
        'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
        'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
        'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
        'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
        'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
        'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'
    ]

    # with open('./input.txt') as t:
    #     INPUT = t.read().splitlines()

    res = countPoints()
    print(res)