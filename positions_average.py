from itertools import combinations

def pos_average(s):
    initial_list = str(s).split(", ")
    perms = list(combinations([x for x, _ in enumerate(initial_list)], 2))
    sum = 0
    for combination in perms:
        for index, char in enumerate(initial_list[combination[0]]):
            if initial_list[combination[1]][index] == char:
                sum += 1

    print(perms)

    return round(sum / (len(initial_list[0]) * len(perms)), 12) * 100


print(pos_average("466960, 069060, 494940, 060069, 060090, 640009, 496464, 606900, 004000, 944096"))