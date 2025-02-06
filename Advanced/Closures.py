'''In Python, a closure is a function that retains access to variables from its enclosing scope, even after the outer function has 
finished executing. Closures are created when a nested function references a value from its enclosing scope.

Key Characteristics of Closures:
Nested Function: A function defined inside another function.

Enclosing Scope: The nested function references a variable from the outer function.

Persistence: The nested function retains access to the variable even after the outer function has completed execution.'''


def outer_function(x):
    def inner_function(y):
        return x + y  # x is from the outer scope, y is the argument of inner_function
    return inner_function  # Return the inner function (closure)

closure = outer_function(12)  
result = closure(5) 
print(result) 


# Practical Use Cases of Closures:
# Function Factories: Create specialized functions dynamically.

def multiplier(x):
    def multiply(n):
        return x*n
    return multiply

double=multiplier(2)
triple=multiplier(3)

print(double(5))
print(triple(5))


# Data Encapsulation: Use closures to encapsulate data and behavior.

def counter():
    count=0
    def increment():
        nonlocal count
        count+=1
        return count
    return increment

counting=counter()

print(counting())
print(counting())

# Callback Functions: Pass closures as callbacks to other functions.

def on_event(callback):
    print("Event Occurred")
    callback()

def create_callback(message):
    def callback():
        print(message)
    return callback

my_callback=create_callback("Hello world")
on_event(my_callback)