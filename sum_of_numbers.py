from functools import reduce

def get_sum(a, b):
    if a != b:
        to_add = list()
        for i in range(a, b + (int((b - a) / abs(b - a))), int((b - a) / abs(b - a))):
            to_add.append(i)
        
        # return to_add
        return reduce(lambda prev, curr: prev + curr, to_add)
    return a

print(get_sum(0, -1))