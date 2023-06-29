import math

def ascend_descend(length, minimum, maximum):
    # print(length, minimum, maximum)
    string = ""
    for num in range(minimum, maximum + 1):
        string += str(num)
    for num in range(maximum - 1, minimum, -1):
        string += str(num)
    print(string)
    if len(string) == 0:
        return ""
    return (math.ceil(length / len(string)) * string)[:length]

print(ascend_descend(14, -4, -5))