# Advent of Code 2019 - Day 2 solution
# Author = Rohith Mohan
# Date = December 04 2019


def calcWireCoordsPartI(x):
    coordsList = []
    curX, curY = 0, 0
    for instr in x.split(','):
        if instr[0] == 'R':
            xIncr, yIncr = 1, 0
        elif instr[0] == 'L':
            xIncr, yIncr = -1, 0
        elif instr[0] == 'U':
            xIncr, yIncr = 0, 1
        elif instr[0] == 'D':
            xIncr, yIncr = 0, -1

        for _ in range(int(instr[1:])):
            curX += xIncr
            curY += yIncr
            coordsList.append((curX, curY))

    return coordsList


def calcWireCoordsPartII(x):
    coordsList = []
    curX, curY = 0, 0
    stepsDict = {}
    step = 0
    for instr in x.split(','):
        if instr[0] == 'R':
            xIncr, yIncr = 1, 0
        elif instr[0] == 'L':
            xIncr, yIncr = -1, 0
        elif instr[0] == 'U':
            xIncr, yIncr = 0, 1
        elif instr[0] == 'D':
            xIncr, yIncr = 0, -1

        for _ in range(int(instr[1:])):
            curX += xIncr
            curY += yIncr
            coordsList.append((curX, curY))
            step += 1
            if (curX, curY) not in stepsDict.keys():
                stepsDict[(curX, curY)] = step

    return coordsList, stepsDict


with open("input.txt", 'r') as input_file:
    wireA_input = input_file.readline()
    wireB_input = input_file.readline()

# Part 1
center = [0, 0]

# wireA_testinput = 'R8,U5,L5,D3'
# wireB_testinput = 'U7,R6,D4,L4'
# wireA_testinput = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
# wireB_testinput = 'U62,R66,U55,R34,D71,R55,D58,R83'
# wireA_testinput = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
# wireB_testinput = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'

wireACoords = calcWireCoordsPartI(wireA_input)
wireBCoords = calcWireCoordsPartI(wireB_input)

intersectionCoords = list(set(wireACoords) & set(wireBCoords))
distance = min([abs(coord[0]) + abs(coord[1]) for coord in intersectionCoords])
print("Part One : " + str(distance))
# Answer for Part One : 260

# Part 2
#wireA_testinput = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
#wireB_testinput = 'U62,R66,U55,R34,D71,R55,D58,R83'
#wireA_testinput = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
#wireB_testinput = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'

wireACoords, wireASteps = calcWireCoordsPartII(wireA_input)
wireBCoords, wireBSteps = calcWireCoordsPartII(wireB_input)

intersectionCoords = list(set(wireACoords) & set(wireBCoords))
distance = min(
    [wireASteps[coord] + wireBSteps[coord] for coord in intersectionCoords])

print("Part Two : " + str(distance))

# Answer for Part Two : 15612
