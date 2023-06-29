def nth_fib(n):
    if n == 1: return 0
    if n == 2 or n == 3: return 1
    val1, val2 = nth_fib(n - 1), nth_fib(n - 2)
    return val1 + val2

print(nth_fib(5))