def gcdi(a,b):
    for num in range(min(a, b)):
        if num % a == 0 and num % b == 0:
            return num

def lcmu(a, b):
    num = max(a, b)
    while (True):
        if a % num == 0 and b % num == 0:
            return num
        num += 1

def som(a, b):
    return a + b
def maxi(a, b):
    return max(a, b)
def mini(a, b):
    return min(a, b)

def oper_array(fct, arr, init):
    prev = init
    output = list()
    for val in arr:
        new = fct(prev, val)
        output.append(new)
        prev = new
    return output