from collections import defaultdict
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



def generateDict(list):
    dic = defaultdict(int)
    for x in list:
        dic[x] += 1
    return dic


def getPriorityScore(items):
    score = 0
    for x in items:
        if(x.islower()):
            score = score + ord(x) - 96
        else:
            score = score + ord(x) -38
    return score

def compareLists3(l1, l2, l3):
    score = 0
    d1 = generateDict(l1)
    d2 = generateDict(l2)
    d3 = generateDict(l3)
    for x1 in d1:
        for x2 in d2:
            if(x1 == x2):
                for x3 in d3:
                    if(x1 == x3):
                        if(x1.islower()):
                            score = score + ord(x1) - 96
                        else:
                            score = score + ord(x1) -38
    return score



total = 0
for line in lines:
    midwayPoint = int(len(line)/2)
    l1 = line[:midwayPoint]
    l2 = line[-midwayPoint:]
    total = total + getPriorityScore(compareLists(l1, l2))
print(total)



def batchLists(items):
    batchedList = []
    tempList = []
    for i in range(1, len(items) + 1):
        tempList.append(items[i-1])
        if(i%3 == 0):
            print(i)
            batchedList.append((tempList[0], tempList[1], tempList[2]))
            tempList = []
    print("batchedlist: ", len(batchedList))
    return batchedList
tot = 0
for batch in batchLists(lines):
    print("__________")
    print(batch)
    tot = tot + compareLists3(batch[0], batch[1], batch[2])
print(tot)