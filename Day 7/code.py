# Advent of Code 2019 - Day 7 solution
# Author = Rohith Mohan
# Date = December 09 2019
from itertools import permutations


def evaluateMode(x, iteration, increment, paramDict):
    if paramDict[increment] == 1:
        return x[iteration + increment]
    else:
        return x[x[iteration + increment]]


def evaluateCode(inputOpCodeList, phase, inputval):
    i = 0
    opCodeInput = None
    x = inputOpCodeList.copy()

    while i < len(x):
        if len(str(x[i])) > 1:
            opCode = int(str(x[i])[-2:])

            paramDict = {1: 0, 2: 0, 3: 0}
            for paramCount in range(len(str(x[i])) - 2):
                paramPosition = -(3 + paramCount)
                paramDict[paramCount + 1] = int(str(x[i])[paramPosition])

        else:
            paramDict = {1: 0, 2: 0, 3: 0}
            opCode = x[i]

        if opCode == 99:
            break
        elif opCode == 1:
            x[x[i + 3]] = evaluateMode(x, i, 1, paramDict) + evaluateMode(
                x, i, 2, paramDict)
            i = i + 4
        elif opCode == 2:
            x[x[i + 3]] = evaluateMode(x, i, 1, paramDict) * evaluateMode(
                x, i, 2, paramDict)
            i = i + 4
        elif opCode == 3:
            if opCodeInput is None:
                opCodeInput = phase
                x[x[i + 1]] = opCodeInput
            else:
                opCodeInput = inputval
                x[x[i + 1]] = opCodeInput
            i = i + 2
        elif opCode == 4:
            # print("x[i]:", x[i], "len(x):", len(x), "i+1:", i + 1, "x[i+1]:",
            #      str(x[i + 1]))
            outputVal = evaluateMode(x, i, 1, paramDict)
            # print("Outputting:", outputVal)
            i = i + 2
        elif opCode == 5:
            if (evaluateMode(x, i, 1, paramDict) != 0):
                i = evaluateMode(x, i, 2, paramDict)
            else:
                i = i + 3
        elif opCode == 6:
            if (evaluateMode(x, i, 1, paramDict) == 0):
                i = evaluateMode(x, i, 2, paramDict)
            else:
                i = i + 3
        elif opCode == 7:
            if (evaluateMode(x, i, 1, paramDict) < evaluateMode(
                    x, i, 2, paramDict)):
                x[x[i + 3]] = 1
            else:
                x[x[i + 3]] = 0
            i = i + 4
        elif opCode == 8:
            if (evaluateMode(x, i, 1,
                             paramDict) == evaluateMode(x, i, 2, paramDict)):
                x[x[i + 3]] = 1
            else:
                x[x[i + 3]] = 0
            i = i + 4
        else:
            raise ValueError("Strange opcode encountered: " + str(x[i]))

    return x, outputVal


with open("input.txt", 'r') as input_file:
    data = input_file.read()

# Part 1

# split on commas and convert to ints
opcodeList = data.split(',')
opcodeList = [int(x) for x in opcodeList]
opcodeListPartI = opcodeList.copy()

signalResults = []
perms = permutations([4, 3, 2, 1, 0])
for perm in perms:
    initialInput = None
    for phase in perm:
        opcodeListPartI = opcodeList.copy()
        if initialInput is None:
            initialInput = evaluateCode(opcodeListPartI, phase, 0)[1]
        else:
            initialInput = evaluateCode(opcodeListPartI, phase,
                                        initialInput)[1]
    signalResults.append(initialInput)

print(max(signalResults))


# Answer for Part One : 34686

# Part 2

# opcodeListPartII = opcodeList.copy()
# evaluateCode(opcodeListPartII, 5)
# Answer for Part Two : 2369720
