import itertools, copy

def possibilities(param):
    pre_perms_list = list()
    question_mark_indexes = list()
    clone = list(copy.deepcopy(param))
    solution = list()

    for index, char in enumerate(param):
        if char == "?":
            pre_perms_list.append([1, 0])
            question_mark_indexes.append(index)
    
    perms = list(itertools.product(*pre_perms_list))
    print(perms)
    for tuple in perms:
        for index, index_of_qn_mark in enumerate(question_mark_indexes):
            clone[index_of_qn_mark] = tuple[index]
        clone = [str(x) for x in clone]
        solution.append("".join(clone))
    
    return solution

print(possibilities('1?1?'))