def multiplication_table(size):
    a = list()
    for i in range(1, size + 1):
        b = list()
        for j in range(1, size + 1):
            b.append(i * j)
        a.append(b)
    
    return a

print(multiplication_table(3))