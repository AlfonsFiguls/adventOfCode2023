import re

def formatInput():
    splitedInp = INPUT.splitlines()
    INSTRUCTIONS = splitedInp[0]
    map = {}
    for e in splitedInp[2:]:
        splited = e.split(' = ')
        values = [m.group() for m in re.finditer(r"[\w]+", splited[1])]
        map[splited[0]] = (values[0], values[1])
    return INSTRUCTIONS, map
        
def countSteps(INSTRUCTIONS, MAP):
    steps = 0
    curr = 'AAA'
    while True:
        for e in INSTRUCTIONS:
            steps += 1
            if e == 'L':
                curr = MAP[curr][0]
            else:
                curr = MAP[curr][1]
            if curr == 'ZZZ':
                return steps
    
def main():
   INSTRUCTIONS, MAP = formatInput()
   steps = countSteps(INSTRUCTIONS, MAP)
   print(steps)

if __name__ == "__main__":
    INPUT = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""
    # with open('./input.txt') as t:
    #     INPUT = t.read()

    main()