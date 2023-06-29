import collections


def scramble(s1, s2):
    counter_for_s2 = dict(collections.Counter(list(s2)))
    counter_for_s1 = dict(collections.Counter(list(s1)))

    try:
        for val in counter_for_s2.keys():
            if counter_for_s1[val] >= counter_for_s2[val]:
                continue
            else:
                return False
        return True
    except KeyError:
        return False

print(scramble("nphfreutflnytlxut", "thlenltlpxt"))