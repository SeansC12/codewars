import re

def valid_parentheses(brackets):
    opening_bracket = "("
    closing_bracket = ")"
    stack = []
    for char in brackets:
        if char == opening_bracket:
            stack.append(char)
        elif char == closing_bracket:
            if len(stack) > 0 and opening_bracket.index(stack.pop()) == closing_bracket.index(char):
                continue
            return False
        else:
            continue
    if brackets.count("(") == brackets.count(")"):
        return True
    return False


print(valid_parentheses("hi())("))