'''1. map(function, iterable)
Applies a function to every item in an iterable and returns an iterator.

Example: Square each element in a list.''' #or Equivalent List Comprehension: [x**2 for x in numbers].

numbers=[1,2,3,4]
squared=map(lambda x:x**2,numbers)
print(list(squared))

'''filter(function, iterable)
Returns an iterator containing elements from the iterable where the function returns True.

Example: Filter even numbers.''' #or Equivalent List Comprehension: [x for x in numbers if x % 2 == 0].

numbers=[1,2,3,4,5,6,7]
even=filter(lambda x:x%2==0,numbers)
print(list(even))

'''3. reduce(function, iterable[, initializer]) (from functools)
Cumulatively applies a function to reduce the iterable to a single value.

Example: Sum all elements.'''

import functools
numbers=[1,2,3,4]
sum=functools.reduce(lambda x,y:x+y,numbers,10)
print(sum)

'''Key Notes:
Lazy Evaluation: map and filter return iterators (Python 3). Use list() to convert results.

Chaining: Combine functions for complex workflows.'''

# result = reduce(lambda x, y: x + y, 
#                 map(lambda x: x**2, 
#                     filter(lambda x: x % 2 == 0, numbers)))

'''Readability: List comprehensions are often clearer for simple cases, but functional constructs excel for chaining or predefined functions.

Edge Cases: Handle empty iterables in reduce with an initializer (e.g., 0 for summing).

When to Use:
map: Apply transformations to elements.

filter: Select elements conditionally.

reduce: Aggregate elements into a single value (when no built-in exists).

These tools enable expressive, functional-style data processing in Python.'''