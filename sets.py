'''In Python, a set is an unordered collection of unique elements. Sets are mutable, meaning you can add or remove elements, 
but the elements themselves must be immutable (e.g., numbers, strings, tuples). Sets are commonly used for tasks like removing 
duplicates, membership testing, and performing mathematical set operations (e.g., union, intersection).

Key Characteristics of Sets
Unordered: Elements in a set do not have a specific order.

Unique: Sets cannot contain duplicate elements.

Mutable: You can add or remove elements from a set.

Elements must be immutable: Set elements must be hashable (e.g., numbers, strings, tuples).'''

# Creating a Set
# You can create a set using curly braces {} or the set() constructor.

# Syntax

# my_set = {element1, element2, element3}  # Using curly braces
# my_set = set(iterable)  # Using the set() constructor

# Creating a set with curly braces
fruits = {"apple", "banana", "cherry"}


# Creating a set from a list (removes duplicates)
numbers = set([1, 2, 2, 3, 4, 4])  # {1, 2, 3, 4}
print(numbers)

# Empty set (use set() instead of {})
empty_set = set()
print(set)


# Common Set Operations
# 1. Adding Elements
# add(element): Adds a single element to the set.
fruits.add("orange")  # {"apple", "banana", "cherry", "orange"}
print(fruits)

# update(iterable): Adds multiple elements from an iterable (e.g., list, tuple).
fruits.update(["mango","grape"])
print(fruits)

# 2. Removing Elements
# remove(element): Removes an element from the set. Raises a KeyError if the element is not found.

fruits.remove("banana")
# fruits.remove('axe')-Raises Error
print(fruits)

# discard(element): Removes an element if it exists. Does not raise an error if the element is not found.
fruits.discard("banana")  # No error if "banana" is not in the set
print(fruits)

# pop(): Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
fruit = fruits.pop()  # Removes and returns a random element
print(fruit)
print(fruits)

# clear(): Removes all elements from the set.
fruits.clear()
print(fruits)


# 3. Set Operations
# Sets support mathematical set operations like union, intersection, difference, and symmetric difference.

# a) Union (| or union())
# Combines elements from two sets, excluding duplicates.

set1={1,2,3}
set2={3,4,5}

# union_set=set1 | set2
union_set=set1.union(set2)
print(union_set)

# b) Intersection (& or intersection())
# Returns elements common to both sets.

# intersection_set= set1 & set2

intersection_set= set1.intersection(set2)

print(intersection_set)

# c) Difference (- or difference())
# Returns elements in the first set that are not in the second set.

# difference_set= set1-set2
difference_set= set1.difference(set2)

print(difference_set)

# d) Symmetric Difference (^ or symmetric_difference())
# Returns elements that are in exactly one of the sets.

# symmetric_set= set1^set2
symmetric_set= set1.symmetric_difference(set2)

print(symmetric_set)

# 4. Set Comparisons
# issubset(): Checks if one set is a subset of another.

set1={1,2}
set2={1,2,3}
print(set1.issubset(set2))

# issuperset(): Checks if one set is a superset of another.

print(set2.issuperset(set1)) 

# isdisjoint(): Checks if two sets have no common elements.
set3 = {4, 5}
print(set1.isdisjoint(set3))  

# Set Comprehensions
# Similar to list comprehensions, you can create sets using set comprehensions.

# Syntax

# {expression for item in iterable if condition}

squares={x**2 for x in range(1,6)}
print(squares)

# Frozen Sets
# A frozen set is an immutable version of a set. Once created, its elements cannot be changed. Frozen sets are hashable and can be used as keys in dictionaries.

# Syntax

# frozen_set = frozenset(iterable)

fruits = frozenset(["apple", "banana", "cherry"])
#fruits.add("orange")  # This will raise an error
print(fruits)

# Example Use Cases
# 1. Removing Duplicates

numbers = [1, 2, 2, 3, 4, 4]
unique_numbers = set(numbers)  # {1, 2, 3, 4}
print(unique_numbers)

# 2. Membership Testing

fruits = {"apple", "banana", "cherry"}
print("apple" in fruits)  

# 3. Mathematical Operations

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # Union
print(set1 & set2)  # Intersection
print(set1 - set2)  # Difference
print(set1^set2)  #symmetric difference
print(set1.issubset(set2))
print(set1.issuperset(set2))
print(set1.isdisjoint(set2))