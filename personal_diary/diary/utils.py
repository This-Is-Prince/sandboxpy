from functools import wraps
import datetime

def logger(func):
    """A decorator that logs when a function is called."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"--- LOG: Calling '{func.__name__}' at {timestamp} ---")
        result = func(*args, **kwargs)
        return result
    
    return wrapper