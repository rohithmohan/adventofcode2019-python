# Advent of Code 2019 - Day 6 solution
# Author = Rohith Mohan
# Date = December 09 2019

# Thought about doing this one without networkx but wow, this is way too elegant to pass up


import networkx as nx

with open("input.txt", 'r') as input_file:
    data = input_file.read()

# Part 1


#testData = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L"
#G = nx.Graph([x.split(')') for x in testData.splitlines()])
#print(sum([nx.shortest_path_length(G,'COM',node) for node in G.nodes]))

G = nx.Graph([x.split(')') for x in data.splitlines()])
print(sum([nx.shortest_path_length(G,'COM',node) for node in G.nodes]))



# Answer for Part One : 295936

# Part 2

#testData = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L\nK)YOU\nI)SAN"
#G = nx.Graph([x.split(')') for x in testData.splitlines()])

print(nx.shortest_path_length(G,'YOU','SAN') - 2)

# Answer for Part One : 457