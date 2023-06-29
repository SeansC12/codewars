import collections
from functools import reduce

def is_valid_walk(walk):
    print(walk)
    counter = dict(collections.Counter(walk))
    for i in "nsew":
        if not i in counter.keys():
            counter[i] = 0
    print(counter)
    try:
        print(reduce(lambda prev, curr: prev + curr, counter.values()))
        return True if counter["n"] == counter["s"] and counter["e"] == counter["w"] and reduce(lambda prev, curr: prev + curr, counter.values()) == 10 else False
    except KeyError:
        return False

print(is_valid_walk(['n', 's']))