'''In Python, iterators are objects that allow you to traverse through all the elements of a collection (like a list, tuple, or 
dictionary) one at a time. They are a fundamental concept in Python and are used extensively in loops, comprehensions, and 
functional programming constructs like map, filter, and reduce.'''

'''Key Concepts
Iterator Protocol:
An iterator is any object that implements the iterator protocol, which consists of two methods:

__iter__(): Returns the iterator object itself.

__next__(): Returns the next value from the iterator. If there are no more items, it raises the StopIteration exception.

Iterable:
An iterable is any object that can return an iterator. Examples include lists, tuples, strings, dictionaries, and sets. 
Iterables implement the __iter__() method, which returns an iterator.

Lazy Evaluation:
Iterators use lazy evaluation, meaning they generate items one at a time and only when needed. 
This makes them memory efficient for large datasets.
'''

'''1. Built-in Iterators
These are iterators provided by Python for common data structures and objects. Examples include:

a) Container Iterators:'''

#   Lists: list_iterator

my_list = [1, 2, 3]
print(list(iter(my_list)))  # Returns a list_iterator

# Tuples: tuple_iterator

my_tuple = (1, 2, 3)
iter(my_tuple)  # Returns a tuple_iterator

# Strings: str_iterator

my_string = "hello"
iter(my_string)  # Returns a str_iterator

# Dictionaries: dict_keyiterator, dict_valueiterator, dict_itemiterator

my_dict = {"a": 1, "b": 2}
iter(my_dict)  # Returns a dict_keyiterator (iterates over keys)
iter(my_dict.values())  # Returns a dict_valueiterator (iterates over values)
iter(my_dict.items())  # Returns a dict_itemiterator (iterates over key-value pairs)

# Sets: set_iterator

my_set = {1, 2, 3}
iter(my_set)  # Returns a set_iterator

# b) File Iterators:

# with open("example.txt", "r") as file:
#     iter(file)  # Returns a file iterator

'''Many Python functions return iterators instead of lists or other collections. Examples include:'''

# a) map:
# Returns an iterator that applies a function to each item of an iterable.

numbers = [1, 2, 3]
squared = map(lambda x: x**2, numbers)  # Returns a map iterator

# b) filter:
# Returns an iterator that includes only items for which a function returns True.

evens = filter(lambda x: x % 2 == 0, numbers)  # Returns a filter iterator

# c) zip:
# Returns an iterator that aggregates elements from multiple iterables.

zipped = zip([1, 2], ["a", "b"])  # Returns a zip iterator

# enumerate:
# Returns an iterator that yields pairs of (index, value) from an iterable.

enumerated = enumerate(["a", "b", "c"])  # Returns an enumerate iterator

# e) range:
# In Python 3, range returns a range object, which is an iterable (not an iterator itself). You can get an iterator from it using iter().
r = range(3)
iter(r)  # Returns a range_iterator

'''3. Iterators from the itertools Module
 The itertools module provides many functions that return iterators for advanced iteration patterns. Examples include:'''

# a) itertools.count:
# Returns an infinite iterator that generates numbers starting from a given value.

import itertools
counter=itertools.count(start=1)

# b) itertools.cycle:
# Returns an infinite iterator that cycles through an iterable.

cycler=itertools.cycle([1,2,3])
for _ in range(10):
    print(next(cycler))

# c) itertools.repeat:
# Returns an iterator that repeats a value indefinitely or a specified number of times.

repeater=itertools.repeat(10,3)

# d) itertools.permutations:
# Returns an iterator that generates all possible permutations of an iterable.

permutations=itertools.permutations([1,2,3])
for i in permutations:
    print(i)

# e) itertools.combinations:
# Returns an iterator that generates all possible combinations of an iterable.

combinations = itertools.combinations([1, 2, 3], 2)  
print(combinations)
for i in combinations:
    print(i)


# 4. Custom Iterators
# You can create your own iterators by defining a class that implements the iterator protocol (__iter__() and __next__() methods).

# Example:

class CountDown:
    def __init__(self,start):
        self.current=start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current<=0:
            raise StopIteration
        else:
            self.current-=1
            return self.current+1
        
countdown=CountDown(3)
for number in countdown:
    print(number)

# 5. Generator Iterators
# Generators are a special kind of iterator created using functions with the yield keyword. They are lazy and generate values on-the-fly.

# Example:

def count_to_top(n):
    current=1
    while current<=n:
        yield current
        current+=1

gen=count_to_top(3)
for i in gen:
    print(i)



    