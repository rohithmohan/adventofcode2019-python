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

# Part 2

# black = 0
# transparent = 2
# white = 1

width = 25
height = 6
layerDim = width * height
results = []

for i in range(int(len(data) / (layerDim))):
    currentLayer = data[layerDim * i:layerDim * (i + 1)]
    results.append(currentLayer)

finalImageFlat = list('x' * layerDim)
for layer in results:
    for pixelIterator in range(len(layer)):
        pixel = layer[pixelIterator]
        if finalImageFlat[pixelIterator] == 'x':
            if pixel == '0':
                finalImageFlat[pixelIterator] = '0'
            elif pixel == '1':
                finalImageFlat[pixelIterator] = '1'

count = 0
finalImage = ""
for x in range(height):
    for y in range(width):
        finalImage = finalImage + finalImageFlat[count].replace('0', ' ')
        count += 1
    finalImage = finalImage + "\n"

print(finalImage)

# Answer for Part Two : GKCKH
# Needed to replace 0 with a blank string to simulate a white background
