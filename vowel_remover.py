def disemvowel(string):
    new_string = list(string)
    print(string)
    for char in string:
        if char in "aeiouAEIOU":
            new_string.remove(char)
    return "".join(new_string)

print(disemvowel("No offense but, Your writing is among the worst I've ever read"))