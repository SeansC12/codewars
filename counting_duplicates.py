import collections

def duplicate_count(text):
    return len(list(filter(lambda val: val > 1, collections.Counter(text.lower()).values())))