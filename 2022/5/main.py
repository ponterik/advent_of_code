import re
import pprint
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


batched_crates = stacks_dict
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
    for _ in range(0, int(times)):
        moveCrate(destination, origin)

#for move in cleaned_moves:
#    moveCreates(destination=move[2], origin=move[1], times = move[0])

def getTopCreates(crates):
    top_values = ""
    for (k, v) in crates.items():
        top_values = top_values + v[len(v)-1]
    return top_values

print("Top creates: " + getTopCreates(stacks_dict))




def move_batch(destination, origin, times):
    crate_stack = batched_crates[origin]
    print(crate_stack)
    print(destination, origin, times)
    moved_stack = crate_stack[(len(crate_stack) - int(times)):]
    print("moving")
    print(moved_stack)
    print("to ", destination, " from ", origin)
    print("Should be ", times, " elements")
    batched_crates[origin] = crate_stack[:(len(crate_stack) - int(times))]
    batched_crates[destination] = batched_crates[destination] + moved_stack

last_move = []
num_moves = 0
for move in cleaned_moves:
    pprint.pprint("_________________")
    pprint.pprint(batched_crates)
    move_batch(destination=move[2], origin=move[1], times = move[0])
    pprint.pprint(batched_crates)
    
pprint.pprint(getTopCreates(batched_crates))