def filter_numbers(num):
    try:
        if (num[0] == "0" and len(num) > 1) or not (int(num) >= 0 and int(num) <= 255) or " " in num or int(num) == -0:
            return False
    except:
        return False
    return True
    

def is_valid_IP(strng):
    print(strng)
    array = strng.split(".")
    new_array = filter(filter_numbers, array)
    new_array = list(new_array)

    if len(new_array) == 4 and len(array) == 4:
        return True
    
    return False


print(is_valid_IP("50.58.22.31"))
