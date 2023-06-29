def to_camel_case(text):
    disallowedCharacters = "-_"
    text2 = list(text)
    for index, value in enumerate(text2):
        if value == "-" or value == "_":
            text2[index + 1] = str(text2[index + 1]).upper()
        else:
            continue

    text = "".join(text2)

    for char in disallowedCharacters:
        text = text.replace(char, "")

    return text

to_camel_case("the-stealth-warrior")
