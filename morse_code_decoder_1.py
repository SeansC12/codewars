MORSE_CODE = {} # THIS IS ONLY TO REMOVE THE WARNING, PURGE WHEN SUBMITTING CODE
import copy

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
    
    print(solution)
    # solution = ['S', 'O', 'S']
    
    if len(solution) > 2:
        solution_original = copy.deepcopy(solution)
        for index, _ in enumerate(solution_original):
            print(solution_original.index(solution_original[-1]))
            
            if index != len(solution_original) - 1:
                solution.insert(index + index + 1, " ")
    
    elif len(solution) == 2:
        solution.insert(1, " ")
    
    return "".join(solution)

print(decode_morse(" . "))