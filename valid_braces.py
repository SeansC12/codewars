def valid_braces(string):
    opening_braces = "([{"
    closing_braces = ")]}"
    stack = []

    if (not ")" in string) and (not "]" in string) and (not "}" in string):
        return False

    for char in string:
        if char in opening_braces:
            stack.append(char)
        else:
            if len(stack) > 0 and opening_braces.index(stack.pop()) == closing_braces.index(char):
                continue
            else:
                return False
    return True

print(valid_braces("{}"))