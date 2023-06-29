import collections

def xo(s):
    dictionary = dict(collections.Counter(s.lower()))
    if not "x" in dictionary and not "o" in dictionary:
        return True
    return dictionary["x"] == dictionary["o"]

print(xo("xxxoo"))