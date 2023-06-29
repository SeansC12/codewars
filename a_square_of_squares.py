import math

def is_square(n):
    try:
        if math.sqrt(n) - int(math.sqrt(n)) == 0:
            return True
        else:
            raise ValueError
    except ValueError:
        return False

print(is_square(3))