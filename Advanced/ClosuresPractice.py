# Exercise 1: Basic Closure (Beginner)
# Write a function greet that takes a name as an argument and returns a closure. 
# The closure should print a greeting message when called.

def greet(name="Guest"):
    def greeting():
        print(f"Hello,{name}")
    return greeting
   

greet_closure = greet("Alice")
greet_closure()  # Output: Hello, Alice!

# Exercise 2: Counter with Step (Intermediate)
# Write a function make_counter that takes a step value as an argument and returns a closure. 
# The closure should increment a counter by the step value each time it is called.

def make_counter(step):
    count=0
    def make_count():
        nonlocal count
        count+=step
        return count
    return make_count

counter = make_counter(2)
print(counter())  # Output: 2
print(counter())  # Output: 4
print(counter())  # Output: 6

# Exercise 3: Power Function Generator (Intermediate)
# Write a function power_function that takes an exponent n and returns a closure.
# The closure should take a number x and return x raised to the power of n.

def power_function(n):
    def powerto(x):
        return x**n
    return powerto

square = power_function(2)
cube = power_function(3)

print(square(4))  
print(cube(3))    

# Exercise 4: Memoization with Closure (Advanced)
# Write a function memoize that takes a function func as an argument and returns a closure. 
# The closure should cache the results of func for previously computed inputs to avoid redundant calculations.

def memoize(func):
    cache={}
    def memoized_func(x):
        if x not in cache:
            cache[x]=func(x)
        return cache[x]
    return memoized_func

def expensive_function(x):
    print(f"Computing {x}...")
    return x * x

memo = memoize(expensive_function)
print(memo(4))  
print(memo(5)) 


# Exercise 5: Function Composition with Closure (Advanced)
# Write a function compose that takes two functions f and g and returns a closure. 
# The closure should apply g to its input and then apply f to the result (i.e., f(g(x))).

def compose(f, g):
    def composed_function(x):
        return f(g(x))
    return composed_function

def add_one(x):
    return x + 1

def square(x):
    return x * x

composed_func = compose(square, add_one)
print(composed_func(3))

# Bonus Exercise: Multiplier Factory (Hard)
# Write a function multiplier_factory that takes a list of numbers and returns a list of closures. 
# Each closure should multiply its input by one of the numbers in the list.

# Example:

def multiplier_factory(numbers):
    multipliers = []
    for num in numbers:
        def multiplier(x, num=num):  # Use default argument to capture num
            return x * num
        multipliers.append(multiplier)
    return multipliers

multipliers = multiplier_factory([2, 3, 4])
print(multipliers[0](5))  
print(multipliers[1](5))  
print(multipliers[2](5))  