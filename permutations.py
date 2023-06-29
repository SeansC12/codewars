import itertools, collections

def permutations(s):
    return set(["".join(x) for x in itertools.permutations(s)])

print(permutations("aabb"))