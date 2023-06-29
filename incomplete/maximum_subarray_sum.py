def max_sequence(arr):
    if len(arr) == 0: return 0
    prev_prev_max = None
    prev_max = None
    current_max = 0
    maxes = list()
    
    for num in arr:
        if prev_prev_max is None or current_max + num >= prev_prev_max:
            current_max += num
            if not prev_max is None: prev_prev_max = prev_max
            prev_max = current_max 
        else:
            maxes.append(current_max)
            prev_prev_max = None
            prev_max = None
            current_max = 0
    
    return max(maxes) if max(maxes) > 0 else 0
    
print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]))