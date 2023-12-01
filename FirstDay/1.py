import re

def findNumbers(e):
    digits = re.findall(r"[\d]", e)
    return int(f"{digits[0]}{digits[-1]}")

def sumOfCalibNums(calibDoc):
    toRet = 0
    for e in calibDoc:
        toRet += findNumbers(e)
    return toRet

if __name__ == "__main__":
    # CALIB_DOC = ['1abc2','pqr3stu8vwx','a1b2c3d4e5f','treb7uchet']
    with open('../calibDoc.txt') as t:
        CALIB_DOC = t.readlines()
    res = sumOfCalibNums(CALIB_DOC)
    print(res)