import io


def get_input():
    with open('./1/input.txt') as f:
        lines = f.readlines()
        return lines
lines = get_input()

prev = int(lines [0]) + int(lines[1]) + int(lines[2])
counter = 0
for i in range(0, len(lines)-2):
    measure = int(lines [i]) + int(lines[i + 1]) + int(lines[i + 2])
    if(prev < measure):
        counter = counter + 1
    prev = measure
print("nr increases:", counter)
    