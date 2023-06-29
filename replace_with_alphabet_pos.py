def alphabet_position(text):
    positions = "abcdefghijklmnopqrstuvwxyz"
    solution = list()
    for char in text:
        try:
            solution.append(positions.index(char.lower()) + 1)
        except ValueError:
            continue
    print(solution)
    return " ".join(str(x) for x in solution)

print(alphabet_position("The sunset sets at twelve o' clock."))