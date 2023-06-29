def open_or_senior(data):
    solution = list()
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            solution.append("Senior")
        else:
            solution.append("Open")
    return solution