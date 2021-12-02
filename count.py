def get_input():
    with open('input.txt') as f:
        lines = f.readlines()
        return lines

lines = get_input()

aggregation = {}
for line in lines:
    dir, value = line.split(" ")
    if dir in aggregation:
        aggregation[dir] = aggregation[dir] + int(value)
    else:
        aggregation[dir] = int(value)

depth = aggregation["down"] - aggregation["up"]
result = aggregation["forward"] * depth
print(result)
    
