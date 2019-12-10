# Advent of Code 2019 - Day 7 solution part 2
# Author = Rohith Mohan
# Date = December 10 2019
from itertools import permutations, chain


def evaluateMode(x, iteration, increment, paramDict):
    if paramDict[increment] == 1:
        return x[iteration + increment]
    else:
        return x[x[iteration + increment]]


def evaluateCode(inputOpCodeList, inputs):
    i = 0
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
            inputval = next(inputs)
            x[x[i + 1]] = inputval
            i = i + 2
        elif opCode == 4:
            # print("x[i]:", x[i], "len(x):", len(x), "i+1:", i + 1, "x[i+1]:",
            #      str(x[i + 1]))
            outputVal = evaluateMode(x, i, 1, paramDict)
            yield outputVal
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

    return None


with open("input.txt", 'r') as input_file:
    data = input_file.read()

# Part 2

# split on commas and convert to ints
opcodeList = data.split(',')
opcodeList = [int(x) for x in opcodeList]
opcodeListPartII = opcodeList.copy()

perms = permutations([9, 8, 7, 6, 5])

maxResult = 0

# Ended up having to use generator and yield, used some of the code from here : https://topaz.github.io/paste/#XQAAAQCMBwAAAAAAAAA0m0pnuFI8c+0tjbUheJzfDHhNSfsqiTbo2Wh+e6U3rkgwkqx8nl7N0nNBTAloRyeoHsZUsUJAsqhpHjlcr57jsanGkYGjcogi4q8v6/yzc9ZflHqjFwHNI6FDZzg1uAAQks1+8RKGdrzBULOY8ZgK6Okp+R1WG/dYfL6DjUoC0txuOH3BeIuUEhH6DjE8HjoHMdqSSsqs4Ols2vWyTgXNvzR1hWPfvJe54XWaZmDiPq2j8liFiF+9lDkcVXpbar7jyEDJz0RDRWYbdhlvj2S7tbuRA0Cbcyih4hNhWjRA3ZEoU5dLuqchOpzLGjl3pG1etwt859wJbzz+7aY5QKgjXWGi5ITud4WDOMYptop3dMSLRt1rNgw+1MHfEcaXA3NdRwCEkY5s89+GVu4K4u0tXCNUMQE6Ch7oHINyi0sDK6VwuXRCSMzOMPmQ5OlfnMoimow68J5pC4R3w9u9/GChExRMNnmpJnswyyE/TEuE+0ijlQjvUr27OR09YtWQMoRKPqKNxb1z9EazkqEL7HXdIJevavkMSr/918W7qZE7W9wiRD9dqKieIYpgefiAH1/9qGGisU3FpMbcwBSUiaNebCJvAP488aLDLXX4WKEcYktj0rscso9JgVeMlvrdmQe5IPGjUoiIk9+Q8SKvXBgriZWqTo7JqWTGjEn1iDzi/RBmynykWajFT/GbcHlySvkmMJvHtTQt3GWqrDS86SjOeSkrSucy3YQIlF1XOkadNUNWS40lzMGbpkpML5P9tnNMwlhD+UY55gXZQqWOtwRkqwtFcJjuihSjjj5rx2skFmdncpfJPLLO3ppnpJRVb+KtjBw/NAJcaYJYfp1unl4ZDMG49ADRfjNjXnQlNAv1w5FL7xZ+oCzQ+Uu0ah+EvM4kjgsCPP1kIOzqwdcRFMx6jSQHfX2tEFQEFyyVaak5QTRJMhXNRtxbInl70sI6OLA3aq4nlPkn/7r7qgU=
# may want to brush up on generators and yield from

for perm in perms:

    def amplifierA():
        yield from evaluateCode(opcodeListPartII,
                                chain(iter([perm[0], 0]), amplifierE()))

    def amplifierB():
        yield from evaluateCode(opcodeListPartII,
                                chain(iter([perm[1]]), amplifierA()))

    def amplifierC():
        yield from evaluateCode(opcodeListPartII,
                                chain(iter([perm[2]]), amplifierB()))

    def amplifierD():
        yield from evaluateCode(opcodeListPartII,
                                chain(iter([perm[3]]), amplifierC()))

    def amplifierE():
        yield from evaluateCode(opcodeListPartII,
                                chain(iter([perm[4]]), amplifierD()))

    results = list(amplifierE())
    if (maxResult < max(results)):
        maxResult = max(results)

print("Part 2 solution:", maxResult)
# Answer for Part Two : 36384144
