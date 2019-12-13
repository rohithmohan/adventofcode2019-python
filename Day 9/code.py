# Advent of Code 2019 - Day 9 solution
# Author = Rohith Mohan
# Date = December 12 2019
# Refactored Day 5 code to incorporate a class (some parts are thanks to Joel Grus' advent code)
from collections import defaultdict
with open("input.txt", 'r') as input_file:
    data = input_file.read()

# Part 1



class EndProgram(Exception): pass

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
            return self.program[self.program[iteration + increment] + self.relative_base]
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
                for paramCount in range(len(str(self.program[self.position])) - 2):
                    paramPosition = -(3 + paramCount)
                    paramDict[paramCount + 1] = int(str(self.program[self.position])[paramPosition])

            else:
                paramDict = {1: 0, 2: 0, 3: 0}
                opCode = self.program[self.position]

            if opCode == 99:
                raise EndProgram
            elif opCode == 1:
                self.program[self.evaluateModeLoc(self.position, 3, paramDict)] = self.evaluateMode(self.position, 1, paramDict) + self.evaluateMode(self.position, 2, paramDict)
                self.position = self.position + 4
            elif opCode == 2:
                self.program[self.evaluateModeLoc(self.position, 3, paramDict)] = self.evaluateMode(self.position, 1, paramDict) * self.evaluateMode(self.position, 2, paramDict)
                self.position = self.position + 4
            elif opCode == 3:
                self.program[self.evaluateModeLoc(self.position, 1, paramDict)] = inputval
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
                    self.position = self.evaluateMode(self.position, 2, paramDict)
                else:
                    self.position = self.position + 3
            elif opCode == 6:
                if (self.evaluateMode(self.position, 1, paramDict) == 0):
                    self.position = self.evaluateMode(self.position, 2, paramDict)
                else:
                    self.position = self.position + 3
            elif opCode == 7:
                if (self.evaluateMode(self.position, 1, paramDict) < self.evaluateMode(self.position, 2, paramDict)):
                    self.program[self.evaluateModeLoc(self.position, 3, paramDict)] = 1
                else:
                    self.program[self.evaluateModeLoc(self.position, 3, paramDict)] = 0
                self.position = self.position + 4
            elif opCode == 8:
                if (self.evaluateMode(self.position, 1, paramDict) == self.evaluateMode(self.position, 2, paramDict)):
                    self.program[self.evaluateModeLoc(self.position, 3, paramDict)] = 1
                else:
                    self.program[self.evaluateModeLoc(self.position, 3, paramDict)] = 0
                self.position = self.position + 4
            elif opCode == 9:
                self.relative_base += self.evaluateMode(self.position, 1, paramDict)
                self.position = self.position + 2
            else:
                raise ValueError("Strange opcode encountered: " + str(self.program[self.position]))

        return self.program



# Answer for Part One : 2671328082 (somehow this messy code works)

# Part 2
opcodeList = data.split(',')
opcodeList = [int(x) for x in opcodeList]
opcodeListPartI = opcodeList.copy()
computer = IntcodeComputer(opcodeListPartI)
outputs = []
inputs = None
testcount = 0
try:
    while True:
        outputs.append(computer.evaluateCode(2))
        inputs = None
except EndProgram:
    print("outputs:", outputs)




# Answer for Part Two : 59095
