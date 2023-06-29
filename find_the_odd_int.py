from collections import Counter

def find_it(seq):
    counter = dict(Counter(seq))
    print(counter)
    for index, val in enumerate(counter.values()):
        if val % 2 != 0:
            return list(counter.keys())[index]

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
