# Advent of Code 2019 - Day 10 solution
# Author = Rohith Mohan
# Date = December 13 2019
from collections import defaultdict
with open("input.txt", 'r') as input_file:
    data = input_file.read()

def evaluateAsteroidCoords(asteroidText):
    asteroidCoords = []
    for row, line in enumerate(asteroidText.splitlines()):
        for col, asteroidFlag in enumerate(line):
            if (asteroidFlag == '#'):
                asteroidCoords.append((row, col))
    return asteroidCoords

def stationLocationFinder(asteroidCoords):
    for asteroid in asteroidCoords:
        print(asteroid)

def getVisibleAsteroids(stationPotentialLocation,asteroidCoords):

example1_Input = ".#..#\n.....\n#####\n....#\n...##"
example1 = evaluateAsteroidCoords(example1_Input)
stationLocationFinder(example1)

# Answer for Part One : 

# Part 2

# Answer for Part Two : 
