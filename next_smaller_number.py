import copy

def next_smaller(n):
    n = str(n)
    x = 0
    y = 0
    n_clone = copy.deepcopy(n)
    
    # identifying x
    for index, _ in reversed(list(enumerate(n_clone))):
        if index != (len(n) - 1) and n[index + 1] < n[index]:
            x = index
            break
    print(n[x])
    
    # identifying y
    new_array = copy.deepcopy(n[x + 1:])

    numbers_bigger_than_x = dict()
    
    for i, num in enumerate(new_array):
        if int(num) < int(n[x]):
            numbers_bigger_than_x[i] = num
    
    if len(numbers_bigger_than_x.values()) != 0:
        y = list(numbers_bigger_than_x.keys())[list(numbers_bigger_than_x.values()).index(max(numbers_bigger_than_x.values()))] + x + 1
    else:
        return -1
    print(n[y])

    # swapping x and y
    n = list(n)
    n[x], n[y] = n[y], n[x]
    # x, y = y, x
    n = "".join(n)
    
    # sorting remaining numbers in descending order
    new_sorting_array = copy.deepcopy(n[x + 1:])
    new_sorting_array = sorted(new_sorting_array, reverse=True)
    print(f"New sorting array {new_sorting_array}")
    
    solution = list()
    solution.append(n[:x + 1])
    solution.append(new_sorting_array)
    solution = [item for sublist in solution for item in sublist]
    
    if len(str(int("".join(solution)))) != len(n):
        return -1
    return int("".join(solution))


print(next_smaller(1027))

# 1247632