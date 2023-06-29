def increment_string(strng):
    original_length = 1
    number = 0
    for index, char in enumerate(strng):
        try:
            new_char = int(char)
            number = int(strng[index:])
            original_length = len(strng) - index
            strng = strng[:index]
        except ValueError:
            continue
    
    number += 1
    return strng + str(number).zfill(original_length)

print(increment_string())