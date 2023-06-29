from itertools import zip_longest

def sum_strings(x, y):
    x, y = x.lstrip("0"), y.lstrip("0")
    carryover = 0
    if len(x) < len(y):
        x = x.zfill(len(y))
    elif len(x) > len(y):
        y = y.zfill(len(x))
    nums = list(reversed(list(zip_longest(x, y, fillvalue=0))))
    sol = ""

    for index, (val1, val2) in enumerate(nums):
        if index == (len(nums) - 1):
            sol += "".join(reversed(str(int(val1) + int(val2) + carryover)))
        else:
            sol += str(int(val1) + int(val2) + carryover)[-1]
            carryover = (int(val1) + int(val2) + carryover) // 10

    return "".join(reversed(list(sol))) if not "".join(reversed(list(sol))) == "" else "0"

print(sum_strings("00103", "08567"))