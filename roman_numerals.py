ones_info = [1, 5, 10]
tens_info = [10, 50, 100]
hundreds_info = [100, 500, 1000]
thousands_info = [1000, 500_000, 1_000_000]

letters = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }

class Table:
    def __init__(self, range):
        if range == "ones":
            self.min = ones_info[0]
            self.mid = ones_info[1]
            self.max = ones_info[2]
            self.current_state = 1
        elif range == "tens":
            self.min = tens_info[0]
            self.mid = tens_info[1]
            self.max = tens_info[2]
            self.current_state = 10
        elif range == "hundreds":
            self.min = hundreds_info[0]
            self.mid = hundreds_info[1]
            self.max = hundreds_info[2]
            self.current_state = 100
        elif range == "thousands":
            self.min = thousands_info[0]
            self.mid = thousands_info[1]
            self.max = thousands_info[2]
            self.current_state = 1000
        

def checkValue(num):
    num = str(num)
    if len(num) == 4:
        return Table("thousands")
    elif len(num) == 3:
        return Table("hundreds")
    elif len(num) == 2:
        return Table("tens")
    elif len(num) == 1:
        return Table("ones")

    # if num / 1000 >= 1:
    #     return Table("thousands")
    # elif num / 1000 <= 1 and num >= 0.1:
    #     return Table("hundreds")
    # elif num / 1000 <= 0.1 and num >= 0.01:
    #     return Table("tens")
    # else:
    #     return Table("ones")

def solution(num):
    i = True
    solution = ""


    roman_alphabet = list(letters.keys())
    roman_number = list(letters.values())

    while i:
        table = checkValue(num)
        initial_state = num

        num -= (int(num) % int(table.current_state))
        copy = num


        if num == table.mid - table.min:
            solution += roman_alphabet[roman_number.index(table.min)] + roman_alphabet[roman_number.index(table.mid)]
            num -= table.mid - table.min
        elif num == table.max - table.min:
            solution += roman_alphabet[roman_number.index(table.min)] + roman_alphabet[roman_number.index(table.max)]
            num -= table.max - table.min
        else:
            while copy > 0:
                try:
                    array = []
                    for value in roman_alphabet:
                        if copy - letters[value] >= 0:
                            array.append(copy - letters[value])
                    position = array.index(min(array))
                    solution += roman_alphabet[position]
                    copy -= roman_number[position]
                    
                except ValueError:
                    break
        
        num = int(initial_state) % int(table.current_state)
        if num == 0:
            i = False
            return solution
        
print(solution(6))