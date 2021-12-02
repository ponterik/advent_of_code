from util_funs import get_input

lines = get_input()
  
aggregation = {"aim": 0, "forward": 0, "depth": 0}
for line in lines:
    dir, value = line.split(" ")
    value = int(value)

    if dir == "up":
        aggregation["aim"] = aggregation["aim"] - value
        
    if dir == "down":
        aggregation["aim"] = aggregation["aim"] + value
    
    if dir == "forward":
        aggregation["forward"] = aggregation["forward"] + value
        aggregation["depth"] = aggregation["depth"] + (aggregation["aim"] * value)

result = aggregation["forward"] * aggregation["depth"]
    
print(result)