def find_pascal_row(row):
    curr_row = list()
    curr_row.append(1)
    
    if row == 0: return curr_row

    prev_row = find_pascal_row(row - 1)

    for num in range(1, len(prev_row)):
        curr_row.append(prev_row[num - 1] + prev_row[num])
    
    curr_row.append(1)

    return curr_row

def expand(expr):
    # finding values from expr
    n = int(str(expr)[str(expr).find("^") + 1:])
    algebraic_term = ""
    if n == 0: return "1"
    a = ""
    for char in expr:
        if char.isalpha():
            a = str(expr)[1:expr.index(char)]
            algebraic_term = char
    # (x-1)^1
    b = int(str(expr)[len(str(a)) + 2:str(expr).find(")")])
    print(f"a: {a}, b: {b}, n: {n}, algebraic_term: {algebraic_term}")
    
    if a == "-":
        a = -1
    elif a == "":
        a = 1
    else:
        a = int(a)
        
    # get coefficients from pascal's triangle row
    coefficients = find_pascal_row(n)
    print(f"pascal triangle row {coefficients}")
    
    # get indices
    indices = list()
    for index, _ in enumerate(coefficients):
        indices.append((n - index, n - (n - index)))
    print(f"indices {indices}")
    
    # evaluate 😎
    solution = ""
    
    for index, tuple in enumerate(indices):
        # first value
        if index == 0:
            coefficient = (a ** tuple[0]) * coefficients[index]
            if coefficient == -1:
                solution += "-"
            elif coefficient == 1:
                solution += ""
            else:
                solution += str(coefficient)
            if tuple[0] == 1:
                solution += f"{algebraic_term}"
            else:
                solution += f"{algebraic_term}^{tuple[0]}"
        # last value
        elif index == len(indices) - 1:
            coefficient = (b ** tuple[1]) * coefficients[index]
            if coefficient >= 1:
                solution += f"+{coefficient}"
            else:
                solution += str(coefficient)
        # values in the middle
        else:
            coefficient = coefficients[index] * (a ** tuple[0]) * (b ** tuple[1])
            if coefficient == -1:
                solution += "-"
            elif coefficient == 1:
                solution += ""
            elif coefficient > 1:
                solution += "+"
                solution += str(coefficient)
            else:
                solution += str(coefficient)
            if tuple[0] == 1:
                solution += f"{algebraic_term}"
            else:
                solution += f"{algebraic_term}^{tuple[0]}"
            
    return solution

print(expand("(x-1)^1"))