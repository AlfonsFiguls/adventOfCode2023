import re
import math

def formatInput():
    splitedInp = INPUT.splitlines()
    INSTRUCTIONS = splitedInp[0]
    map = {}
    initial = []
    for e in splitedInp[2:]:
        splited = e.split(' = ')
        values = [m.group() for m in re.finditer(r"[\w]+", splited[1])]
        map[splited[0]] = (values[0], values[1])
        if splited[0].endswith('A'):
            initial.append(splited[0])
    return INSTRUCTIONS, map, initial

def countSteps(INSTRUCTIONS, MAP, curr):
    steps = 0
    while True:
        for e in INSTRUCTIONS:
            steps += 1
            if e == 'L':
                curr = MAP[curr][0]
            else:
                curr = MAP[curr][1]
            if curr.endswith('Z'):
                return steps
    
def main():
   INSTRUCTIONS, MAP, INITIAL = formatInput()
   indSteps = []
   for e in INITIAL:
    indSteps.append(countSteps(INSTRUCTIONS, MAP, e))
   print(math.lcm(*indSteps))

if __name__ == "__main__":
    INPUT = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""
    # with open('./input.txt') as t:
    #     INPUT = t.read()

    main()