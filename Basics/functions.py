'''In Python, a function is a block of reusable code that performs a specific task. 
Functions help in organizing code, making it more modular, and easier to read and maintain. 
You can define your own functions or use built-in functions provided by Python.

Defining a Function
You can define a function using the def keyword, followed by the function name, parentheses (), and a colon :. 
The code block within the function is indented.'''
'''
def function_name(parameters):
    # Function body
    # Perform some operations
    return result  # Optional'''

# def: Keyword to define a function.

# function_name: Name of the function (follows Python naming conventions).

# parameters: Inputs to the function (optional).

# return: Used to return a value from the function (optional). If omitted, the function returns None.

def greet(name):
    return f"Hello, {name}!"

# Calling the function
message = greet("Raj")
print(message)  

# Parameters and Arguments:

# Parameters are variables listed in the function definition.

# Arguments are the values passed to the function when it is called.

def add(a, b):  # a and b are parameters
    return a + b

result = add(3, 5)  # 3 and 5 are arguments
print(result) 

# Default Arguments:
# You can provide default values for parameters.

def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet()) 
print(greet("Bob")) 

# Keyword Arguments:
# You can pass arguments by specifying the parameter name.

def describe_person(name, age):
    return f"{name} is {age} years old."

print(describe_person(age=25, name="Alice")) 

# Variable-Length Arguments:

# *args: Allows you to pass a variable number of non-keyword arguments.

# **kwargs: Allows you to pass a variable number of keyword arguments.


def print_args(*args):
    for arg in args:
        print(arg)

print_args(1,2,3)


def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_kwargs(name="Alice", age=25)

# Return Values:
# A function can return one or more values using the return statement. If no return statement is provided, the function returns None.

def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result) 

# Lambda Functions:
# Lambda functions are small, anonymous functions defined using the lambda keyword.

squares=lambda x:x**2
print(squares(5))

# Scope of Variables:

# Local Scope: Variables defined inside a function are local to that function.

# Global Scope: Variables defined outside all functions are global and can be accessed anywhere.

x = 10  # Global variable

def my_function():
    y = 5  # Local variable
    print(x + y)

my_function() 


