def order(sentence):
    words = list(sentence.split(" "))
    number_array = []
    solution = []

    for i in words:
        for x in i:
            try:
                x = int(x)
                number_array.append(x)
            except ValueError:
                continue

    fixed_num_array_length = len(number_array)
    
    for i in range(fixed_num_array_length):
        index = number_array.index(min(number_array))
        solution.append(words[index])
        number_array[index] = 1000
        
    return " ".join(solution)

print(order("4of Fo1r pe6ople g3ood th5e the2"))