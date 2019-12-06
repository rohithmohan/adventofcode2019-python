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


def evaluateCode(x):
    i = 0
    while i < len(x):
        if len(str(x[i])) > 1:
            opCode = int(str(x[i])[-2:])
            print("opcode:", opCode)
            paramDict = {1: 0, 2: 0, 3: 0}
            for paramCount in range(len(str(x[i])) - 2):
                paramPosition = -(3 + paramCount)
                paramDict[paramCount + 1] = int(str(x[i])[paramPosition])
                print("paramDict", paramDict)
                print("paramCount:",paramCount)

        else:
            paramDict = {1: 0, 2: 0, 3: 0}
            opCode = x[i]

        if opCode == 99:
            break
        elif opCode == 1:
            # x[x[i + 3]] = x[x[i + 1]] + x[x[i + 2]]
            x[x[i + 3]] = evaluateMode(x, i, 1, paramDict) + evaluateMode(
                x, i, 2, paramDict)
            i = i + 4
        elif opCode == 2:
            # x[x[i + 3]] = x[x[i + 1]] * x[x[i + 2]]
            x[x[i + 3]] = evaluateMode(x, i, 1, paramDict) * evaluateMode(
                x, i, 2, paramDict)
            i = i + 4
        elif opCode == 3:
            print("Input required, passing 1 to input")
            x[x[i + 1]] = 1
            i = i + 2
        elif opCode == 4:
            print("Outputting: " + str(x[x[i + 1]]))
            i = i + 2

        else:
            raise ValueError("Strange opcode encountered: " + str(x[i]))

    return x


evaluateCode(opcodeListPartI)

# Answer for Part One : 13933662 (somehow this messy code works)


# Answer for Part Two : 6979
