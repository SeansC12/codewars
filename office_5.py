from functools import reduce

def meeting(rooms, need):
    print(need)
    if need == 0:
        return "Game On"
    sol = list()
    
    for room in rooms:
        if len(sol) >= 1 and reduce(lambda prev, curr: prev + curr, sol) >= need:
            break
        sol.append(max(0, room[1] - len(room[0])))
    
    print(sol)
    
    if reduce(lambda prev, curr: prev + curr, sol) > need:
        if len(sol) > 1:
            sol.pop()
            new_last_count = need - reduce(lambda prev, curr: prev + curr, sol)
            sol.append(new_last_count)
            return sol
        else:
            sol.pop()
            new_last_count = need
            sol.append(new_last_count)
            return sol
    elif reduce(lambda prev, curr: prev + curr, sol) == need:
        return sol
    return "Not enough!"

print(meeting([['XXXXXX', 7], ['', 10], ['', 5], ['XXXXX', 1], ['XXXXXX', 5], ['XXXXXXX', 6], ['XXXX', 10], ['XXX', 7], ['XX', 10], ['XXXX', 5]], 2))