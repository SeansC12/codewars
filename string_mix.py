import collections

def mix(s1, s2):
    solution = ""
    count_arr_1 = list()
    count_arr_2 = list()
    s1_alphabets = list(filter(lambda char: char in "abcdefghijklmnopqrstuvwxyz", s1))
    s2_alphabets = list(filter(lambda char: char in "abcdefghijklmnopqrstuvwxyz", s2))
    counter_1 = dict(collections.Counter(s1_alphabets))
    counter_2 = dict(collections.Counter(s2_alphabets))

    # ensure that both dictionaries have the same letters
    print(list(max(list(counter_1.keys()), list(counter_2.keys()))))

    for char in list(counter_1.keys()):
        try:
            if max(counter_1[char], counter_2[char]) <= 1:
                counter_1.pop(char, None)
                counter_2.pop(char, None)
                continue
        except KeyError:
            if counter_1[char] <= 1:
                counter_1.pop(char, None)
                continue
            elif counter_1[char] > 1:
                count_arr_1.append("1")
                count_arr_2.append(counter_1[char] * char)
                continue
        
        count_in_a = counter_1[char]
        count_in_b = counter_2[char]

        if count_in_a > count_in_b:
            count_arr_1.append("1")
            count_arr_2.append(count_in_a * char)
        elif count_in_a < count_in_b:
            count_arr_1.append("2")
            count_arr_2.append(count_in_b * char)
        else:
            count_arr_1.append("=")
            count_arr_2.append(count_in_a * char)
    
    for char in list(counter_2.keys()):
        try:
            if max(counter_1[char], counter_2[char]) <= 1:
                counter_1.pop(char, None)
                counter_2.pop(char, None)
                continue
        except KeyError:
            if counter_2[char] <= 1:
                counter_2.pop(char, None)
                continue
        if not char in counter_1.keys():
            count_arr_1.append("2")
            count_arr_2.append(counter_2[char] * char)

    print(f"counter 1: {counter_1}, counter 2: {counter_2}")
    
    # sorting stage 3: alphabetical order
    count_arr_1 = [x for _, x in sorted(zip(count_arr_2, count_arr_1), key=lambda pair: pair[0])]
    count_arr_2 = sorted(count_arr_2)

    # sorting stage 2: lexicographic order
    count_arr_2 = [x for _, x in sorted(zip(count_arr_1, count_arr_2), key=lambda pair: pair[0])]
    count_arr_1 = sorted(count_arr_1)
    
    # sorting stage 1: alphabetical count
    count_arr_1 = [x for _, x in sorted(zip(count_arr_2, count_arr_1), key=lambda pair: len(pair[0]), reverse=True)]
    count_arr_2 = sorted(count_arr_2, key=lambda item: len(item), reverse=True)
    # print(count_arr_1, count_arr_2)

    for index, prefix in enumerate(count_arr_1):
        solution += f"{prefix}:{count_arr_2[index]}"
        if not index == len(count_arr_1) - 1:
            solution += "/"

    return solution

print(mix("Lords of the Fallen", "gamekult"))