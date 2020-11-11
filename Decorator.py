import functools


def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do somthing
        value = func(*args, **kwargs)
        # Do somthing after
        return value

    return wrapper_decorator
