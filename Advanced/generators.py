'''Generators in Python are a special type of iterator that allow you to generate values on-the-fly (lazily) 
instead of storing them all in memory. They are created using functions with the yield keyword or generator expressions. 
Generators are memory-efficient and ideal for working with large datasets or infinite sequences.'''

# Key Concepts
# 1. Creating a Generator
# Use a function with the yield keyword.

# When the generator function is called, it returns a generator object (not the values directly).

def countdown(n):
    while n>0:
        yield n #pause here , save the state, return the value.
        n-=1

gen=countdown(5)
print(gen)
for i in gen:
    print(i)

# 2. How Generators Work
# yield pauses the function, saves its state, and returns a value.

# On the next call to next(), execution resumes from where it left off.

# When the function ends, StopIteration is raised.

def simplegenerator():
    yield 'a'
    yield 'b'
    yield 'c'

gen1=simplegenerator()
print(list(gen1))
# print(next(gen1)) # raises error.


# 3. Memory Efficiency
# Generators do not store all values in memory at once. They generate values one at a time.

# Example: Read a large file line by line without loading it entirely into memory:

# def read_large_file(file_path):
#     with open(file_path, "r") as file:
#         for line in file:
#             yield line.strip()

# # Process lines one by one
# for line in read_large_file("huge_data.txt"):
#     process(line)


# 4. Generator Expressions
# Similar to list comprehensions but use () instead of [].

# They return a generator object (lazy evaluation).

# List comprehension (stores all values in memory)
squares_list = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Generator expression (generates values on-the-fly)
squares_gen = (x**2 for x in range(5))
print(list(squares_gen))

    
# 5. Chaining Generators
# Generators can be chained to create data pipelines.

def even_numbers(numbers):
    for num in numbers:
        if num%2==0:
            yield num

def squared_numbers(numbers):
    for num in numbers:
        yield num**2

numbers=[2,3,4,5,6,7,8,9,11,12]
chain_gen=squared_numbers(even_numbers(numbers))
print(list(chain_gen))

# Common Use Cases

# Large Datasets:
# def process_large_data(data):
#     for item in data:
#         yield process(item)  # Process one item at a time

# Infinite Sequences:
def infinite_counter():
    count = 0
    while True:
        yield count
        count += 1

counter = infinite_counter()


# Stateful Iteration:

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a,b=b,a+b

fib=fibonacci()
for _ in range(10):
    print(next(fib))

