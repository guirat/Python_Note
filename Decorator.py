
def my_decorator(func):
  def wrapper():
    func()
  return wrapper


@my_decorator
def my_function():
  return "OK"*
  
