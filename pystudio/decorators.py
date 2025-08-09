import time
from functools import wraps

def simple_decorator(func):
    print("Simple decorator")

    def wrapper():
        print("Starting Wrapper...")
        func()
        print("Ending Wrapper...")

    return wrapper


def say_hello():
    name = "Prince"
    print(f"Hello, {name}")

wrapper = simple_decorator(say_hello)


wrapper()
print()

@simple_decorator
def say_goodbye():
    print("Goodbye!")

say_goodbye()

print()

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"'{func.__name__}' ran in: {end_time - start_time:.4f} seconds")
        return result
    
    return wrapper

@timer
def example_task(n):
    """A simple task that takes some time."""
    total = 0
    for i in range(n):
        total += i
    return total

example_task(1000000)

print(example_task.__name__)
print(example_task.__doc__)

print()