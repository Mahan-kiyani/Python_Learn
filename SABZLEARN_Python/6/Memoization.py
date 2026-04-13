# Memoization
from functools import wraps

def memoize(func):
    memory = {}
    @wraps(func)
    def decorator_fib(n):
        if n not in memory:
            memory[n] = func(n)  
        return memory[n]
    
    return decorator_fib

@memoize
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(3))