def find_nb(m):
    total = 0
    current_cube = 1
    while total < m:
        total += current_cube ** 3
        current_cube += 1
    if total == m:
        return current_cube - 1
    else:
        return -1


print(find_nb(225))