def get_input():
    with open('input.txt') as f:
        lines = f.readlines()
        return lines
lines = get_input()

prev = int(lines.pop(0))
counter = 0
for line in lines:
    measure = int(line)
    if(prev <= measure):
        counter += 1
        print(measure, " increased")
    prev = measure
print("nr increases:", counter)
    
