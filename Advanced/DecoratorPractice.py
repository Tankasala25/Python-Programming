'''1. Basic: Create a Simple Decorator
Task:
Write a decorator simple_decorator that prints "Before function execution" before calling the function and 
"After function execution" after the function call.'''

def simple_decorator(func):
    def wrapper(*args,**kwargs):
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper


@simple_decorator
def say_hello():
    print("Hello!")

say_hello()


# 2.


def message_decorator(func):
    def wrapper(*args,**kwargs):
        print("Before function execution")
        func(*args,**kwargs)
        print("After function execution")
    return wrapper


@message_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


# 4. More Advanced: Multiple Decorators
# Task:
# Create two decorators:

# uppercase_decorator: Converts the output of the function to uppercase.
# repeat_decorator: Calls the function twice.
# Apply both decorators to a function.

def repeat_decorator(times):
    def uppercase_decorator(func):
        def wrapper(*args,**kwargs):
            result=func(*args,**kwargs).upper()
            return '\n'.join([result for _ in range(times)])      
        return wrapper
    return uppercase_decorator
        
@repeat_decorator(times=2)
def welcome():
    return "Hello, welcome!"

print(welcome())


# 5. Expert Level: Class-Based Decorator
# Task:
# Implement a class-based decorator called CountCalls that counts how many times a function has been called.

from functools import wraps
def CountCalls(func):
    count=0
    @wraps(func)
    def wrapper(*args,**kwargs):
        nonlocal count
        count=count+1
        result=func(*args,**kwargs)
        print(f"Function {func.__name__} has been called {count} times.")
        return result
    return wrapper
        
@CountCalls
def hello():
    print("Hello!")

hello()
hello()
hello()

# Question 3: "Execution Time Decorator"

import time

def timer_decorator(func):
    def wrapper(*args,**kwargs):

        start_time=time.time()
        result=func(*args,**kwargs)
        end_time=time.time()
        executed_time=start_time-end_time
        print(f"Function {func.__name__} took {executed_time:.4f} seconds to execute.")
        return result
    return wrapper

@timer_decorator
def compute():
    sum([i**2 for i in range(10000000)])

compute()
