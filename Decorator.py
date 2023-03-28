from time import time

def decorator(func):
    def wrapper(s: str):
        start = time()
        result = func(s)
        finish = time() - start
#        print(f'Result: {result}\tTime: {finish*1000000000:.3} ns')
        return result
    return wrapper