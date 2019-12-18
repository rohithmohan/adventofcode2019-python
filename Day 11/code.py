# Advent of Code 2019 - Day 11 solution
# Author = Rohith Mohan
# Date = December 17 2019
# Joel Grus' live code sessions were helpful for interpreting the problem

from collections import defaultdict
with open("input.txt", 'r') as input_file:
    data = input_file.read()

# Part 1


class EndProgram(Exception):
    pass


class IntcodeComputer:
    def __init__(self, program):
        self.program = defaultdict(int)
        self.program.update({i: value for i, value in enumerate(program)})
        self.relative_base = 0
        self.position = 0
        self.loopcounter = 0

    def evaluateMode(self, iteration, increment, paramDict):

        if paramDict[increment] == 1:
            return self.program[iteration + increment]
        elif paramDict[increment] == 2:
            return self.program[self.program[iteration + increment] +
                                self.relative_base]
        else:
            return self.program[self.program[iteration + increment]]

    def evaluateModeLoc(self, iteration, increment, paramDict):

        if paramDict[increment] == 1:
            return iteration + increment
        elif paramDict[increment] == 2:
            return self.program[iteration + increment] + self.relative_base
        else:
            return self.program[iteration + increment]

    def evaluateCode(self, inputval):
        while True:
            self.loopcounter += 1
            if len(str(self.program[self.position])) > 1:
                opCode = int(str(self.program[self.position])[-2:])

                paramDict = {1: 0, 2: 0, 3: 0}
                for paramCount in range(
                        len(str(self.program[self.position])) - 2):
                    paramPosition = -(3 + paramCount)
                    paramDict[paramCount + 1] = int(
                        str(self.program[self.position])[paramPosition])

            else:
                paramDict = {1: 0, 2: 0, 3: 0}
                opCode = self.program[self.position]

            if opCode == 99:
                raise EndProgram
            elif opCode == 1:
                self.program[self.evaluateModeLoc(
                    self.position, 3, paramDict)] = self.evaluateMode(
                        self.position, 1, paramDict) + self.evaluateMode(
                            self.position, 2, paramDict)
                self.position = self.position + 4
            elif opCode == 2:
                self.program[self.evaluateModeLoc(
                    self.position, 3, paramDict)] = self.evaluateMode(
                        self.position, 1, paramDict) * self.evaluateMode(
                            self.position, 2, paramDict)
                self.position = self.position + 4
            elif opCode == 3:
                self.program[self.evaluateModeLoc(self.position, 1,
                                                  paramDict)] = inputval
                self.position = self.position + 2
            elif opCode == 4:
                #print("x[self.position]:", self.program[self.position], "len(x):", len(self.program), "self.position+1:", self.position + 1, "x[self.position+1]:",
                #    str(self.program[self.position + 1]))
                outputVal = self.evaluateMode(self.position, 1, paramDict)
                #print("Outputting: " + str(outputVal))
                self.position = self.position + 2
                return outputVal
            elif opCode == 5:
                #print("program:",self.program)
                if (self.evaluateMode(self.position, 1, paramDict) != 0):
                    self.position = self.evaluateMode(self.position, 2,
                                                      paramDict)
                else:
                    self.position = self.position + 3
            elif opCode == 6:
                if (self.evaluateMode(self.position, 1, paramDict) == 0):
                    self.position = self.evaluateMode(self.position, 2,
                                                      paramDict)
                else:
                    self.position = self.position + 3
            elif opCode == 7:
                if (self.evaluateMode(self.position, 1, paramDict) <
                        self.evaluateMode(self.position, 2, paramDict)):
                    self.program[self.evaluateModeLoc(self.position, 3,
                                                      paramDict)] = 1
                else:
                    self.program[self.evaluateModeLoc(self.position, 3,
                                                      paramDict)] = 0
                self.position = self.position + 4
            elif opCode == 8:
                if (self.evaluateMode(self.position, 1,
                                      paramDict) == self.evaluateMode(
                                          self.position, 2, paramDict)):
                    self.program[self.evaluateModeLoc(self.position, 3,
                                                      paramDict)] = 1
                else:
                    self.program[self.evaluateModeLoc(self.position, 3,
                                                      paramDict)] = 0
                self.position = self.position + 4
            elif opCode == 9:
                self.relative_base += self.evaluateMode(
                    self.position, 1, paramDict)
                self.position = self.position + 2
            else:
                raise ValueError("Strange opcode encountered: " +
                                 str(self.program[self.position]))

        return self.program


def calcAbsoluteDirection(currentDirection, newRelativeDirection):
    if currentDirection == 0:
        if newRelativeDirection == 0:
            return 3
        else:
            return 1
    elif currentDirection == 1:
        if newRelativeDirection == 0:
            return 0
        else:
            return 2
    elif currentDirection == 2:
        if newRelativeDirection == 0:
            return 1
        else:
            return 3
    elif currentDirection == 3:
        if newRelativeDirection == 0:
            return 2
        else:
            return 0


def calcNewPosition(panelGridCoord, newDirection):
    if newDirection == 0:
        return panelGridCoord[0], panelGridCoord[1] + 1
    elif newDirection == 1:
        return panelGridCoord[0] + 1, panelGridCoord[1]
    elif newDirection == 2:
        return panelGridCoord[0], panelGridCoord[1] - 1
    elif newDirection == 3:
        return panelGridCoord[0] - 1, panelGridCoord[1]


opcodeList = data.split(',')
opcodeList = [int(x) for x in opcodeList]
opcodeListPartI = opcodeList.copy()

computer = IntcodeComputer(opcodeListPartI)

panelGrid = defaultdict(int)
paintedPanels = set()

panelGridCoord = (0, 0)
# panelGrid[panelGridCoord] = 0
panelGrid[panelGridCoord] = 1

currentDirection = 0
stepsTaken = 0

try:
    while True:
        stepsTaken += 1
        currentColor = panelGrid[panelGridCoord]
        newColor = computer.evaluateCode(currentColor)
        newRelativeDirection = computer.evaluateCode(None)

        paintedPanels.add(panelGridCoord)
        panelGrid[panelGridCoord] = newColor

        newDirection = calcAbsoluteDirection(currentDirection,
                                             newRelativeDirection)
        panelGridCoord = calcNewPosition(panelGridCoord, newDirection)

        currentDirection = newDirection

except EndProgram:
    print(len(set(paintedPanels)))

# Answer for Part One : 2469

# Part 2

drawTop, drawRight = -999999, -999999
drawBottom, drawLeft = 999999, 999999
for coordVal, colorVal in panelGrid.items():
    if colorVal == 1:
        drawTop = max(drawTop, coordVal[1])
        drawRight = max(drawRight, coordVal[0])
        drawBottom = min(drawBottom, coordVal[1])
        drawLeft = min(drawLeft, coordVal[0])

for col in range(drawTop, drawBottom - 1, -1):
    for row in range(drawLeft, drawRight + 1):
        if panelGrid[(row, col)] == 1:
            print("*", end="")
        if panelGrid[(row, col)] == 0:
            print(" ", end="")
    print("")
# Answer for Part Two : KLCZAEGU
