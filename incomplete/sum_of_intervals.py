def sum_of_intervals(intervals):
    new_array = [item for sublist in intervals for item in sublist]
    number_line = dict()
    
    for i in range(min(new_array), max(new_array) + 1):
        number_line[i] = 0
    
    for sublist in intervals:
        for index, _ in enumerate(sublist):
            if index == 0:
                continue
            else:
                number_line[index] += 1
    
    solution = 0
    for i in list(number_line.values()):
        if i > 0:
            solution += 1
    return solution