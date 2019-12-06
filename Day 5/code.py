# Advent of Code 2019 - Day 5 solution
# Author = Rohith Mohan
# Date = December 05 2019

with open("input.txt", 'r') as input_file:
    data = input_file.read()

# Part 1

# split on commas and convert to ints
opcodeList = data.split(',')
opcodeList = [int(x) for x in opcodeList]
opcodeListPartI = opcodeList.copy()


def evaluateMode(x, iteration, increment, paramDict):
    if paramDict[increment] == 1:
        return x[iteration + increment]
    else:
        return x[x[iteration + increment]]


def evaluateCode(x, inputval):
    i = 0
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
            x[x[i + 1]] = inputval
            i = i + 2
        elif opCode == 4:
            print("x[i]:", x[i], "len(x):", len(x), "i+1:", i + 1, "x[i+1]:",
                  str(x[i + 1]))
            print("Outputting: " + str(evaluateMode(x, i, 1, paramDict)))
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

    return x


# evaluateCode(opcodeListPartI)

# Answer for Part One : 13933662 (somehow this messy code works)

# Part 2

opcodeListPartII = opcodeList.copy()
evaluateCode(opcodeListPartII, 5)
# Answer for Part Two : 2369720
