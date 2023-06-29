import timeit

def square(n):
    return n * n

def pi_fract(n, t):
    if n == 0:
        return square(((t) * 2 - 1) + (t))
    return ((t - n + 1) * 2 - 1) + square((t - n + 1)) / pi_fract(n - 1, t)

start = timeit.default_timer()
val = 4.0 / pi_fract(100, 100)
stop = timeit.default_timer()

print(val)
print(stop - start)

def pi_cont_frac(n):
    def inner(n):
        if n == 0:
            return lambda d: 4 / d
        else:
            return lambda d: inner(n-1)(2*n - 1 + (n*n / (d)))
    return inner(n)(1)

start = timeit.default_timer()
val2 = pi_cont_frac(100)
stop = timeit.default_timer()

print(val2)
print(stop - start)