# Decorators in Python
# A decorator in Python is a design pattern that allows the modification of functions or methods without changing their actual code. 
# Decorators are widely used for logging, access control, memoization, and more.

'''1. What is a Decorator?
A decorator is essentially a function that takes another function as an argument and 
extends its behavior without explicitly modifying it.'''

def my_decorator(func):
    def wrapper():
        print("Before the function execution")
        func()
        print("After the execution of function.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, World!")

say_hello()

# 3. Decorators with Arguments
# If the decorated function takes arguments, the wrapper function must also accept those arguments.

def repeat_decorator(func):
    def wrapper(*args,**kwargs):
        print("repeat the function")
        func(*args,**kwargs)
    return wrapper

@repeat_decorator
def greet(name):
    print(f"Hello, {name}")

greet("Alice")

# 4. Using functools.wraps
# When using decorators, the original function's metadata (name, docstring) is lost. To preserve it, use functools.wraps.

from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("before the function execution")
        result=func(*args,**kwargs)
        print("After the function execution")
        return result
    return wrapper
@my_decorator
def add(a,b):
    """adding two numbers a,b"""
    return a+b

print(add(5,10))
print(add.__name__)
print(add.__doc__)


# 5. Decorators with Parameters
# If you need to pass arguments to a decorator, wrap it inside another function.

def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(times):
                func(*args,**kwargs)
        return wrapper
    return decorator
    
@repeat(times=3)
def greet(name):
    print(f"Hello, {name}")

greet("Bob")


class MyDecorator:
    def __init__(self,func):
        self.func=func

    def __call__(self,*args, **kwargs):
        print("Before execution of function")
        result=self.func(*args,**kwargs)
        print("After the execution of program")
        return result
    
@MyDecorator
def greet(name):
    print(f"Hello , {name}")

greet("Alice")


# 7. Built-in Decorators
# Python provides several built-in decorators:

# @staticmethod
# Defines a static method inside a class that doesn’t access instance or class variables.

class MathOperations:
    @staticmethod
    def add(a,b):
        return a+b;

print(MathOperations.add(5,3))
obj=MathOperations()
print(obj.add(5,3))



class Example:
    count=0

    @classmethod
    def increment(cls):
        cls.count+=1
        return cls.count
    
print(Example.increment())
print(Example.increment())


class Circle:
    def __init__(self,radius):
        self._radius=radius

    @property
    def area(self):
        return 3.14*self._radius**2
    
c=Circle(5)
print(c.area)
        


    
    

    
        
