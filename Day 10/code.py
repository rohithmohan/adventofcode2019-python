# Advent of Code 2019 - Day 10 solution
# Author = Rohith Mohan
# Date = December 17 2019

import math
from collections import defaultdict, OrderedDict

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
    visibleAsteroids = {}

    for targetCoords in asteroidCoords:
        # print("targetCoords =", targetCoords)
        if stationPotentialLocation == targetCoords:
            continue

        dx = stationPotentialLocation[0] - targetCoords[0]
        dy = stationPotentialLocation[1] - targetCoords[1]

        gcdVal = math.gcd(dx, dy)
        dx = dx / gcdVal
        dy = dy / gcdVal

        if (dx, dy) not in visibleAsteroids:
            visibleAsteroids[(dx, dy)] = targetCoords

    return visibleAsteroids


def getLaserVaporizations(station, asteroidCoords):
    asteroidsToBeVaporized = defaultdict(list)

    for targetCoords in asteroidCoords:
        # print("targetCoords =", targetCoords)
        if station == targetCoords:
            continue

        dx = station[0] - targetCoords[0]
        dy = station[1] - targetCoords[1]

        gcdVal = math.gcd(dx, dy)
        dx = dx / gcdVal
        dy = dy / gcdVal

        # Set top to 0 degrees / pi/2 radians
        radianToBeStored = math.atan2(dy, dx) - math.radians(90)
        # Get rid of negative radians by adding by 2pi and then getting
        # remainder after dividing by 2pi
        radianToBeStored = (math.radians(360) +
                            radianToBeStored) % math.radians(360)

        asteroidsToBeVaporized[radianToBeStored].append(targetCoords)

    for concurrentAsteroids in asteroidsToBeVaporized.values():
        concurrentAsteroids.sort(key=lambda aster: abs(aster[0] - station[0]) +
                                 abs(aster[1] - station[1]),
                                 reverse=True)

    asteroidsToBeVaporizedSorted = OrderedDict(
        sorted(asteroidsToBeVaporized.items()))
    resultsCoords = []

    while asteroidsToBeVaporizedSorted:
        # Had to make copy through list otherwise orderdeddict has mutate error
        radianKeys = list(asteroidsToBeVaporizedSorted.keys())
        for radianKey in radianKeys:
            if asteroidsToBeVaporizedSorted[radianKey]:
                resultsCoords.append(
                    asteroidsToBeVaporizedSorted[radianKey].pop())
            else:
                del asteroidsToBeVaporizedSorted[radianKey]

    return resultsCoords


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
# Answer for Part One : 326, coords (22, 28)

# Part 2

example6_Input = ".#....#####...#..\n##...##.#####..##\n##...#...#.#####.\n..#.....X...###..\n..#.#.....#....##"
example6 = evaluateAsteroidCoords(example6_Input)

# results = getVisibleAsteroids((8, 3), example6)
# print(results.values())
# print(results[(7.0, 3.0)])
# getLaserVaporizations((8, 3),example6)
# print(getLaserVaporizations((11, 13),example5)[199]) # ((8,2))
print(getLaserVaporizations((22, 28), partI)[199])  # (16,23)
# Answer for Part Two :1623
