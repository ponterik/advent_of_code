def get_input(path):
    with open(path) as f:
        lines = f.readlines()
        strippedValues = list(map(lambda x: x.strip(), lines))
        return strippedValues