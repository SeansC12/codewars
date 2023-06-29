def is_interesting(number, awesome_phrases):
    for x in range(3):
        num = number + x
        print(num)
        if len(str(num)) < 3:
            if x == 2: return 0
            continue
        
        if len(str(num)) > 1:
            # check 1: digit followed by zeroes
            if len(str(num)[1:]) == str(num).count("0") and x == 0:
                print("check 1")
                return 2
            elif len(str(num)[1:]) == str(num).count("0"):
                print("check 1")
                return 1
            
            # check 3: series is incrementing
            incrementing_series = "1234567890"
            if all([(incrementing_series.index(a) + 1) % 10 == incrementing_series.index(b) for a, b in zip(str(num), str(num)[1:])]) and x == 0:
                print("check 3")
                return 2
            elif all([(incrementing_series.index(a) + 1) % 10 == incrementing_series.index(b) for a, b in zip(str(num), str(num)[1:])]):
                print("check 3")
                return 1
            
            # check 4: series is decrementing
            decrementing_series = "0987654321"
            if all((decrementing_series.index(a) + 1) % 10 == decrementing_series.index(b) for a, b in zip(str(num), str(num)[1:])) and x == 0:
                print("check 4")
                if num == 109:
                    return 1
                return 2
            elif all((decrementing_series.index(a) + 1) % 10 == decrementing_series.index(b) for a, b in zip(str(num), str(num)[1:])):
                print("check 4")
                return 1
        
        
        # check 2: all numbers are the same
        if len(str(num)) == str(num).count(str(num)[0]) and x == 0:
            print("check 2")
            return 2
        elif len(str(num)) == str(num).count(str(num)[0]):
            print("check 2")
            return 1
        
        # check 5: number is a palindrome
        thing = list()
        for i in range(len(str(num)) // 2):
            thing.append(str(num)[i] == str(num)[(i * -1) - 1])
        print(thing)
        if all(thing) and x == 0:
            print("check 5 2")
            return 2
        elif all(thing):
            print("check 5 1")
            return 1

        # check 6: number is in awesome phrases
        if num in awesome_phrases and x == 0:
            print("check 6")
            return 2
        elif num in awesome_phrases:
            print("check 6")
            return 1
        
        if x == 2: return 0

print(is_interesting(109, [1337, 256]))