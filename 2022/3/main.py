import io

def get_input():
    with open('./2022/3/input.txt') as f:
        lines = f.readlines()
        strippedValues = list(map(lambda x: x.strip(), lines))
        return strippedValues
lines = get_input()

def compareLists(l1, l2):
    items = set()
    for x in l1:
        for y in l2:
            if(x == y):
                items.add(x)
    return items

def getPriorityScore(items):
    score = 0
    for x in items:
        if(x.islower()):
            score = score + ord(x) - 96
        else:
            score = score + ord(x) -38
    return score
total = 0
for line in lines:
    midwayPoint = int(len(line)/2)
    l1 = line[:midwayPoint]
    l2 = line[-midwayPoint:]
    total = total + getPriorityScore(compareLists(l1, l2))
print(total)
