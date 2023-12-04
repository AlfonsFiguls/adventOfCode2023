import re

def returnNumList(e):
    return [m.group() for m in re.finditer(r"[\d]+", e)]

def returnCardPoints(nums, wNums):
    points = 0
    for n in nums:
        if n in wNums:
            if points == 0:
                points = 1
            else:
                points *= 2
    return points

def countPoints():
    toRet = 0
    for e in INPUT:
        splited = e.split('|')
        wNums = returnNumList(splited[0].split(': ')[1])
        nums = returnNumList(splited[1])
        toRet += returnCardPoints(nums, wNums)
    return toRet

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