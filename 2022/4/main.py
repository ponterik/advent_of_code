def get_input():
    with open('./2022/4/input.txt') as f:
        lines = f.readlines()
        strippedValues = list(map(lambda x: x.strip(), lines))
        return strippedValues
lines = get_input()
splitted = [v.split(",") for v in lines]
cleaned = [[ [int(x) for x in value.split("-")] for value in pair ] for pair in [v.split(",") for v in lines]]

#print(splitted_values)

cnt = 0
for c in cleaned:
    if c[0][1] >= c[1][1] and c[0][0] <= c[1][0]:
        cnt = cnt + 1
    elif c[0][1] <= c[1][1] and c[0][0] >= c[1][0]:
        cnt = cnt + 1

print(cnt)

def compareInRange(min, max, num):
    return min <= num and max >= num


cnti = 0
for c in cleaned:
    (min1, max1, min2, max2) = (c[0][0], c[0][1], c[1][0], c[1][1])
    if compareInRange(min1, max1, min2) or compareInRange(min1, max1, max2) or compareInRange(min2, max2, min1) or compareInRange(min2, max2, max1):
        cnti = cnti + 1



print(cnti)