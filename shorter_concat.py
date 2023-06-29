def shorter_reverse_longer(a,b):
    shorter = ""
    longer = ""
    if len(a) > len(b):
        shorter = b
        longer = a
    elif len(a) < len(b):
        shorter = a
        longer = b
    else:
        shorter = b
        longer = a
    return f"{shorter}{longer[::-1]}{shorter}"