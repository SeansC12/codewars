import collections

def count(string):
    return dict(collections.Counter(list(string)))