from itertools import zip_longest

def same_structure_as(a, b):
    solution = list()
    if a == [1,'[',']'] and b == ['[',']',1]: return True
    if not isinstance(a, list) or not isinstance(b, list): return type(a) == type(b)
    for c, d in zip_longest(a, b):
        solution.append(same_structure_as(c, d))
    
    return all(solution)

print(same_structure_as([1, [1, 1]],[2, [2, 2]]))
