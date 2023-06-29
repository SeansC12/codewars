def get_sum(n):
    output = 0
    for num in range(1, n + 2):
        if num % 2 == 1:
            output += (num * num) + (num * (num - 1))
        else:
            output += (-num * num) - (num * (num - 1))
    return output

print(get_sum(3))