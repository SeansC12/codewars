def tribonacci(signature, n):
    if n > 3:
        solution = list(signature)
        for index in range(3, n):
            solution.append(sum(solution[index - 3:index]))
        return solution
    else:
        return signature[:n]

print(tribonacci([1, 1, 1], 10))