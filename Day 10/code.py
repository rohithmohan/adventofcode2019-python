# Advent of Code 2019 - Day 10 solution
# Author = Rohith Mohan
# Date = December 16 2019

import math

with open("input.txt", 'r') as input_file:
    data = input_file.read()


def evaluateAsteroidCoords(asteroidText):
    asteroidCoords = []
    for row, line in enumerate(asteroidText.splitlines()):
        for col, asteroidFlag in enumerate(line):
            if (asteroidFlag == '#'):
                asteroidCoords.append((col, row))
    return asteroidCoords


def stationLocationFinder(asteroidCoords):
    bestStation = None
    bestStationCount = 0
    for asteroid in asteroidCoords:
        visibileCount = len(getVisibleAsteroids(asteroid, asteroidCoords))
        if visibileCount > bestStationCount:
            bestStation = asteroid
            bestStationCount = visibileCount
    return bestStation, bestStationCount


def getVisibleAsteroids(stationPotentialLocation, asteroidCoords):
    visibleAsteroids = []

    for targetCoords in asteroidCoords:
        # print("targetCoords =", targetCoords)
        if stationPotentialLocation == targetCoords:
            continue

        dx = stationPotentialLocation[0] - targetCoords[0]
        dy = stationPotentialLocation[1] - targetCoords[1]

        gcdVal = math.gcd(dx, dy)
        dx = dx / gcdVal
        dy = dy / gcdVal

        # print("targetCoords =", targetCoords, "dx=", dx, "dy=", dy)
        visibleAsteroids.append((dx, dy))

    return list(set(visibleAsteroids))


# print("The gcd of -15 and -10 is : ", math.gcd(-15, -10))

example1_Input = ".#..#\n.....\n#####\n....#\n...##"
example1 = evaluateAsteroidCoords(example1_Input)
assert stationLocationFinder(example1)[0] == (3, 4)
assert stationLocationFinder(example1)[1] == 8

example2_Input = "......#.#.\n#..#.#....\n..#######.\n.#.#.###..\n.#..#.....\n..#....#.#\n#..#....#.\n.##.#..###\n##...#..#.\n.#....####"
example2 = evaluateAsteroidCoords(example2_Input)
assert stationLocationFinder(example2)[0] == (5, 8)
assert stationLocationFinder(example2)[1] == 33

example3_Input = "#.#...#.#.\n.###....#.\n.#....#...\n##.#.#.#.#\n....#.#.#.\n.##..###.#\n..#...##..\n..##....##\n......#...\n.####.###."
example3 = evaluateAsteroidCoords(example3_Input)
assert stationLocationFinder(example3)[0] == (1, 2)
assert stationLocationFinder(example3)[1] == 35

example4_Input = ".#..#..###\n####.###.#\n....###.#.\n..###.##.#\n##.##.#.#.\n....###..#\n..#.#..#.#\n#..#.#.###\n.##...##.#\n.....#.#.."
example4 = evaluateAsteroidCoords(example4_Input)
assert stationLocationFinder(example4)[0] == (6, 3)
assert stationLocationFinder(example4)[1] == 41

example5_Input = ".#..##.###...#######\n##.############..##.\n.#.######.########.#\n.###.#######.####.#.\n#####.##.#.##.###.##\n..#####..#.#########\n####################\n#.####....###.#.#.##\n##.#################\n#####.##.###..####..\n..######..##.#######\n####.##.####...##..#\n.#####..#.######.###\n##...#.##########...\n#.##########.#######\n.####.#.###.###.#.##\n....##.##.###..#####\n.#.#.###########.###\n#.#.#.#####.####.###\n###.##.####.##.#..##"
example5 = evaluateAsteroidCoords(example5_Input)
assert stationLocationFinder(example5)[0] == (11, 13)
assert stationLocationFinder(example5)[1] == 210

partI = evaluateAsteroidCoords(data)
print(stationLocationFinder(partI))
# Answer for Part One : 326

# Part 2

# Answer for Part Two :
