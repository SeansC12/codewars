# return masked string
def maskify(cc):
    if len(cc) > 4:
        new_string = cc[:-4]
        print(new_string)
        for i in new_string:
            new_string = new_string.replace(str(i), "#")
        new_string += cc[-4:]
        return new_string
    else:
        return cc
    pass

print(maskify(input()))