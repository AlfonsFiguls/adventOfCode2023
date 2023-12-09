import re
from functools import reduce

def checkAllZeros(e):
    return all(x==0 for x in e)

def calcHistory(e):
    e = [int(m.group()) for m in re.finditer(r"[-\d]+", e)]
    sequences = [e]
    while not checkAllZeros(sequences[-1]):
        toAdd = []
        for i,x in enumerate(sequences[-1][:-1]):
            toAdd.append(sequences[-1][i+1] - x)
        sequences.append(toAdd)
    for i in range(1,len(sequences)):
        seqPos = -1*(i+1)
        lastPos = -1*i
        sequences[seqPos] = [sequences[seqPos][0] - sequences[lastPos][0]] + sequences[seqPos]
    return sequences[0][0]

def main():
    h = []
    for e in INPUT:
        h.append(calcHistory(e))
    print(reduce(lambda x, y: x + y, h))

if __name__ == '__main__':
    INPUT = [
        '0 3 6 9 12 15',
        '1 3 6 10 15 21',
        '10 13 16 21 30 45'
    ]
    # with open('./input.txt') as t:
    #     INPUT = t.read().splitlines()
    main()