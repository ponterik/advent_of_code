import re

def get_input(path):
    with open(path) as f:
        lines = f.readlines()
        strippedValues = list(map(lambda x: x.strip(), lines))
        return strippedValues

def get_lines(path):
    with open(path) as f:
        lines = f.readlines()
        return lines
        
moves = get_input('./2022/5/moves.txt')


stacks = get_lines('./2022/5/stacks.txt')
index_line = stacks.pop()


indexes = {}
for i in range(0, len(index_line)):
    if(index_line[i].isnumeric()):
        indexes[index_line[i]] = i

stacks_dict = {}

#Init dict
for (c, i) in indexes.items():
        stacks_dict[c] = []

for row in stacks:
    for (c, i) in indexes.items():
        if(row[i] != ' '):
            stacks_dict[c] = [row[i]] + stacks_dict[c]



cleaned_moves = []
for move in moves:
    moves_to_append = []
    for word in move.split():
        if(word.isnumeric()):
            moves_to_append =  moves_to_append + [word]
    if(moves_to_append != []):
        cleaned_moves = cleaned_moves + [moves_to_append]
        moves_to_append = []


def moveCrate(destination, origin):
    crate = stacks_dict[origin].pop()
    stacks_dict[destination].append(crate)

def moveCreates(destination, origin, times):
    for i in range(0, int(times)):
        moveCrate(destination, origin)

for move in cleaned_moves:
    moveCreates(destination=move[2], origin=move[1], times = move[0])

def getTopCreates():
    top_values = ""
    for (k, v) in stacks_dict.items():
        top_values = top_values + v[len(v)-1]
    return top_values

print("Top creates: " + getTopCreates())
