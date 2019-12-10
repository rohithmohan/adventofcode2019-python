# Advent of Code 2019 - Day 8 solution
# Author = Rohith Mohan
# Date = December 10 2019

with open("input.txt", 'r') as input_file:
    data = input_file.read()

# Part 1

width = 25
height = 6

layerDim = width * height

results = []

minZeroCount = 1000000
bestResult = None

for i in range(int(len(data) / (layerDim))):
    currentLayer = data[layerDim * i:layerDim * (i + 1)]
    results.append(currentLayer)
    if currentLayer.count('0') < minZeroCount:
        minZeroCount = currentLayer.count('0')
        bestResult = currentLayer.count('1') * currentLayer.count('2')

print(bestResult)

# Answer for Part One : 1463

