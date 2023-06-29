def alphanumeric(password):
    if len(password) < 1: return False
    for i in password:
        if not str(i).lower() in "abcdefghijklmnopqrstuvwxyz1234567890":
            return False
    return True