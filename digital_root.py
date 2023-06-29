from functools import reduce

def digital_root(n):
    counter = 0
    n = list(str(n))
    n = [ int(i) for i in n ]
    print(n)

    counter = reduce(lambda prev, curr: prev + curr, n)

    while len(str(counter)) > 1:
        counter2 = list(str(counter))
        counter2 = [ int(i) for i in counter2 ]
        counter = reduce(lambda prev, curr: prev + curr, counter2)

    return(counter)
    # while len(n) > 1:
    #     counter += reduce(lambda prev, curr: prev + curr, n)
    #     print(counter)
    #     if len(str(counter)) > 1:
    #         n = list(str(counter))
    #         continue
        
    #     n = list(str(counter))
    #     print(n)
    # return int(n[0])

print(digital_root(13215))