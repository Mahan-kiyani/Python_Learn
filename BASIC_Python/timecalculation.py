from time import perf_counter
from functools import wraps

def time_calculation(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        print(f'run time off {func.__name__} is = {run_time}')
        return value
    return inner

@time_calculation
def name():
    pass

name()
