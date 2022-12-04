from util_funs import get_input

lines = get_input()

aggregation = {}
for line in lines:
    dir, value = line.split(" ")
    if dir in aggregation:
        aggregation[dir] = aggregation[dir] + int(value)
    else:
        aggregation[dir] = int(value)
print(aggregation["down"])
print(aggregation["up"])
depth = aggregation["down"] - aggregation["up"]
result = aggregation["forward"] * depth
print(result)
    
