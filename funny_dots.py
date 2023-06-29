def dot(width, height):
    border = "+---" * width + "+"
    zeroes = "| o " * width + "|"
    solution = ""
    for row in range(height):
        solution += border
        solution += "\n"
        solution += zeroes
        solution += "\n"
    solution += border
    return solution

print(dot(2, 2))