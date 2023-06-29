def parse(data):
    output = list()
    curr = 0

    for char in data:
        if char == "i":
            curr += 1
        elif char == "d":
            curr -= 1
        elif char == "s":
            curr = curr ** 2
        elif char == "o":
            output.append(curr)
    return output