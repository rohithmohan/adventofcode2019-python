# Advent of Code 2019 - Day 1 solution
# Author = Rohith Mohan
# Date = December 03 2019
import math

with open("input.txt", 'r') as input_file:
    data = input_file.read()

# Part 1
# 1) Split as newline char
# 2) Divide by three and use floor to round down
# 3) Subtract by 2 and enclose in parenthesis to enforce Order of Ops
# 4) Use list comprehension and sum the list

partOneResult = sum([(math.floor(int(x) / 3) - 2) for x in data.split('\n')])

print("Part One : " + str(partOneResult))
# Answer for Part One : 3224048

# Part 2
# Turn above into recursive function


def calcFuel(x):
    result = math.floor(int(x) / 3) - 2

    if result > 0:
        return result + calcFuel(result)
    else:
        return 0


partTwoResult = sum([calcFuel(x) for x in data.split('\n')])

print("Part Two : " + str(partTwoResult))
# Answer for Part Two : 4833211
