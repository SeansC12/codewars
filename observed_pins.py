import itertools
import functools

adjacent_numbers = {
    1: [1, 2, 4],
    2: [1, 2, 5, 3],
    3: [3, 2, 6],
    4: [4, 1, 5, 7],
    5: [5, 2, 4, 6, 8],
    6: [6, 3, 5, 9],
    7: [7, 4, 8],
    8: [8, 0, 5, 7, 9],
    9: [9, 6, 8],
    0: [0, 8]
}

def get_pins(observed):
    perms = list()
    for char in observed:
        perms.append(adjacent_numbers[int(char)])
    solution = list(itertools.product(*list(x for x in perms)))
    print(solution)

    for index, tuple in enumerate(solution):
        new_tuple = "".join(str(x) for x in tuple)
        solution.pop(index)
        solution.insert(index, str(new_tuple))

    return solution

print(get_pins('007'))