import collections, functools

def top_3_words(text):
    entire_text = list(text.lower())
    current_word = ""
    words = list()
    for char in entire_text:
        if str(char).isalpha() or char == "'":
            current_word += char
        else:
            if current_word != "": words.append(current_word)
            current_word = ""
    if current_word != "": words.append(current_word)
    
    for word in words:
        if list(filter(lambda char: char.isalpha(), word)) == []:
            words.remove(word)
    
    print(words)

    counter = collections.Counter(words)
    return [i[0] for i in counter.most_common(3)]
    

print(top_3_words("  '''  "))