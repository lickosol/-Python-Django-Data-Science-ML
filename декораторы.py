#логирование данных

from functools import wraps

def log_function_call(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"Function name: {fn.__name__}")
        print(f"Function arguments: {args}, {kwargs}")
        result = fn(*args, **kwargs)
        print(f"Function result: {result}")
        return result
    return wrapper

@log_function_call
def mult(a, b):
    return a * b

print(mult(5, 2))


#проверка аргументов


