def delete_nth(order, max_e):
    sol = list()
    for num in order:
        if sol.count(num) < max_e:
            sol.append(num)
    return sol

print(delete_nth([20,37,20,21], 1))