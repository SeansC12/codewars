def up_array(arr):
    for num in arr:
        if len(str(num)) > 1:
            return None
    try: return [int(x) for x in list(str(int("".join([str(x) for x in arr])) + 1))] 
    except ValueError: return None