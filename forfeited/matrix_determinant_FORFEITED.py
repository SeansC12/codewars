def calculateSimpleMatrix(a, b, c, d):
    return (a * d) - (b * c)

def determinant(matrix):
    if len(matrix) == 2:
        a, b = matrix[0]
        c, d = matrix[1]
        return calculateSimpleMatrix(a, b, c, d)
    elif len(matrix) == 3:
        a, b, c = matrix[0]
        d, e, f = matrix[1]
        g, h, i = matrix[2]
        return (a * calculateSimpleMatrix(e, f, h, i)) - (b * calculateSimpleMatrix(d, f, g, i) + (c * calculateSimpleMatrix(d, e, g, h)))
    else:
        return matrix[0][0]

print(determinant([[2,4,2],[3,1,1],[1,2,0]]))