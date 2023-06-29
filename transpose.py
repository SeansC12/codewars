def transpose(matrix):
    end_matrix = list()
    for _ in matrix[0]:
        end_matrix.append([])
    for i in matrix:
        for index, j in enumerate(i):
            end_matrix[index].append(j)
    
    return end_matrix

print(transpose([[1]]))
