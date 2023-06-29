import math

def is_prime(num):
    if num <= 1: return False
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            return False
    return True

print(is_prime(177))