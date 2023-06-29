from collections import Counter
import copy
from functools import reduce

def decode_bits(bits):
    step = 1
    current_count = 0
    count_list = list()
    morse_code = ""

    print(bits)

    # 1 1 0 0 1 1 0 0 1 1 0 0 0 0 0 0

    for position, _ in enumerate(bits):
        if bits[position - step] != bits[position] and position != 0:
            count_list.append(current_count)
            current_count = 0
        current_count += 1
    count_list.append(current_count)
    print(count_list)



    if max(count_list) % 7 == 0:
        seven_time_units = max(count_list)
        three_time_units = seven_time_units / 7 * 3
        one_time_unit = seven_time_units / 7
    elif max(count_list) % 3 == 0:
        seven_time_units = max(count_list) / 3 * 7
        three_time_units = max(count_list)
        one_time_unit = max(count_list) / 3
    else:
        seven_time_units = max(count_list) * 7
        three_time_units = max(count_list) * 3
        one_time_unit = max(count_list)

    for for_loop_index, count in enumerate(count_list):
        if count == seven_time_units:
            morse_code += "   "
            continue

        elif count == three_time_units:
            list_of_numbers_till_count = copy.deepcopy(count_list[:for_loop_index + 1])
            index = reduce(lambda a, b: a + b, list_of_numbers_till_count)
            if bits[index - 1] == "1":
                morse_code += "-"
            else:
                morse_code += " "

        elif count == one_time_unit:
            list_of_numbers_till_count = copy.deepcopy(count_list[:for_loop_index + 1])
            index = reduce(lambda a, b: a + b, list_of_numbers_till_count)
            if bits[index - 1] == "1":
                morse_code += "."
            else:
                continue
    
    return morse_code


# ···· · −·−−   ·−−− ··− −·· ·
# '1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'                

def decode_morse(morse_code):
    solution = list()
    words_array = morse_code.split("   ")
    
    for word in words_array:
        characters = word.split(" ")
        final_word = ""
        if word == "":
            list(words_array).remove(word)
            continue

        for char in characters:
            if char != "":
                final_word += str(MORSE_CODE[char]).upper()
            else:
                list(characters).remove(char)
                continue
        solution.append(final_word)
    
    if len(solution) > 2:
        solution_original = copy.deepcopy(solution)
        for index, _ in enumerate(solution_original):
            print(solution_original.index(solution_original[-1]))
            
            if index != len(solution_original) - 1:
                solution.insert(index + index + 1, " ")
    
    elif len(solution) == 2:
        solution.insert(1, " ")
    
    return "".join(solution)

print(decode_morse(decode_bits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')))