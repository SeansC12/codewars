import collections

def permute_a_palindrome(input):
    counter = dict(collections.Counter(input))
    
    if len(input) == 3 and input[0] == input[1] == input[2]:
        return True
    elif len(input) == 2 and input[0] == input[1]:
        return True
    
    for i in list(counter.keys()):
        if counter[i] == 1:
            del counter[i]
            break
    
    print(counter)
    for i in counter.values():
        if i % 2 == 0:
            continue
        else:
            return False
    return True
    
print(permute_a_palindrome("abcdefghba"))