def solution(s):
    s = list(s)
    for index, char in enumerate(s):
        if index != (len(s) - 1) and char != " " and not str(char).isupper() and str(s[index + 1]).isupper():
            s.insert(index + 1, " ")
    return "".join(s)

print(solution("brCelCase"))