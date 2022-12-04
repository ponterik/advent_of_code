import io

def get_input():
    with open('./2022/1/input.txt') as f:
        lines = f.readlines()
        return lines
lines = get_input()

strippedValues = list(map(lambda x: x.strip(), lines))

#list(map(lambda x: print(x), map(int, map(lambda x: x.strip(), lines))))
max = 0
old_max = 0
max_values = []
temp_values = []
counter = 0
for x in strippedValues:
    temp_values.append(x)
    if(x == ''):
        counter = counter + 1
        if(max > old_max):
            print(max)
            old_max = max
            max_values = temp_values
        temp_values = []
        max = 0
    else:
        max = max + int(x)
print("old max: ", old_max)
print(max_values)
print(counter)