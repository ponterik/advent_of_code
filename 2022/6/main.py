def get_input(path):
    with open(path) as f:
        lines = f.readlines()
        strippedValues = list(map(lambda x: x.strip(), lines))
        return strippedValues[0]




def detect_unique_message_index(input, length):
    window = []
    for i in range(0, len(input)):
        if(len(set(window)) == length):
            print(window)
            print(i)
            return i
        if(len(window) <= length - 1):
            window =  window + [input[i]]
        elif(len(window) > length - 1):
            window.pop(0)
            window =  window + [input[i]]
        #print(window)
detect_unique_message_index(get_input('./2022/6/input.txt'), 4)

detect_unique_message_index(get_input('./2022/6/input.txt'), 14)

