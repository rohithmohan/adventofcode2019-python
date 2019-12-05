# Advent of Code 2019 - Day 4 solution
# Author = Rohith Mohan
# Date = December 05 2019


def passwordCheckPart1(x):
    prevNum = None
    doubleFlag = None
    for digit in str(x):
        if prevNum:
            if int(digit) < prevNum:
                return 0
            if int(digit) == prevNum:
                doubleFlag = 1
            prevNum = int(digit)
        else:
            prevNum = int(digit)

    if doubleFlag:
        return 1
    else:
        return 0


def passwordCheckPart2(x):
    prevNum = None
    dupDict = {}
    for digit in str(x):
        if prevNum:
            if int(digit) < prevNum:
                return 0
            if int(digit) == prevNum:
                if int(digit) in dupDict:
                    dupDict[int(digit)] += 1
                else:
                    dupDict[int(digit)] = 1

            prevNum = int(digit)
        else:
            prevNum = int(digit)

    if 1 in dupDict.values():
        return 1
    else:
        return 0


with open("input.txt", 'r') as input_file:
    beginning, end = input_file.readline().split('-')

# Part 1
passwordCount = 0
for password in range(int(beginning), int(end)):
    if (passwordCheckPart1(password)):
        passwordCount += 1

print("Part One : " + str(passwordCount))
# Answer for Part One : 1767

# Part 2
passwordCount = 0
for password in range(int(beginning), int(end)):
    if (passwordCheckPart2(password)):
        passwordCount += 1

print("Part Two : " + str(passwordCount))

# Answer for Part Two : 1192
