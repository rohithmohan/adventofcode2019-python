# Advent of Code 2019 - Day 2 solution
# Author = Rohith Mohan
# Date = December 04 2019

with open("input.txt", 'r') as input_file:
    data = input_file.read()

# Part 1

# split on commas and convert to ints
opcodeList = data.split(',')
opcodeList = [int(x) for x in opcodeList]


# define function for evaluating opcode
# use while loop so that it's possible to skip around iterator
def evaluateCode(x):
    i = 0
    while i < len(x):
        if x[i] == 99:
            break
        elif x[i] == 1:
            x[x[i + 3]] = x[x[i + 1]] + x[x[i + 2]]
            i = i + 4
        elif x[i] == 2:
            x[x[i + 3]] = x[x[i + 1]] * x[x[i + 2]]
            i = i + 4
        else:
            raise ValueError("Strange opcode encountered: " + str(x[i]))

    return x


# tests written based on puzzle prompt
def testsPart1():
    assert [2, 0, 0, 0, 99] == evaluateCode([1, 0, 0, 0, 99])
    assert [2, 3, 0, 6, 99] == evaluateCode([2, 3, 0, 3, 99])
    assert [2, 4, 4, 5, 99, 9801] == evaluateCode([2, 4, 4, 5, 99, 0])
    assert [30, 1, 1, 4, 2, 5, 6, 0,
            99] == evaluateCode([1, 1, 1, 4, 99, 5, 6, 0, 99])
    assert [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40,
            50] == evaluateCode([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])

    return "Tests passed"


print(testsPart1())

# Return data to state prior to alarm
opcodeList[1] = 12
opcodeList[2] = 2

print("Part One : " + str(evaluateCode(opcodeList)[0]))
# Answer for Part One : 3931283

print("Part Two : " + str())
# Answer for Part Two :
