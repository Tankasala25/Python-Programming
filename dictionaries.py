'''In Python, a dictionary is a powerful and versatile data structure that stores data in key-value pairs.
Dictionaries are unordered (in Python versions before 3.7) and mutable, meaning you can add, remove, 
or modify key-value pairs after creation. They are highly optimized for fast lookups and are commonly used for storing
and retrieving data efficiently.'''

# Creating a Dictionary
# Dictionaries are created using curly braces {} or the dict() constructor. Each key-value pair is separated by a colon :

# Creating a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Using the dict() constructor
another_dict = dict(name='bob',age=30,city='London')

# Accessing Dictionary Elements
# You can access values in a dictionary using their keys.

my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Accessing values
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])   # Output: 25

# Using the get() method (avoids KeyError if the key doesn't exist)
print(my_dict.get("city"))  # Output: New York
print(my_dict.get("country", "Unknown"))  # Output: Unknown (default value)

# Adding and Modifying Elements
# You can add new key-value pairs or modify existing ones.

# Adding a new key-value pair
my_dict["country"] = "USA"

# Modifying an existing value
my_dict["age"] = 26

print(my_dict)
# Output: {"name": "Alice", "age": 26, "city": "New York", "country": "USA"}

# Removing Elements
# You can remove key-value pairs using the following methods:

# 1. pop(key)
# Removes the key-value pair for the specified key and returns the value. Raises a KeyError if the key is not found.

age = my_dict.pop("age")  # Removes "age" and returns value 26
print(age)
print(my_dict)

# 2. popitem()
# Removes and returns the last inserted key-value pair (in Python 3.7+). In earlier versions, it removes an arbitrary pair.

last_item = my_dict.popitem()  # Removes and returns ("country", "USA")
print(last_item)
print(my_dict)

# 3. del statement
# Deletes a key-value pair or the entire dictionary.

del my_dict["city"]  # Removes the "city" key
print(my_dict)
del my_dict  # Deletes the entire dictionary

my_dict = {"name": "Alice", "age": 25, "city": "New York"}
# 4. clear()
# Removes all key-value pairs from the dictionary, making it empty.

my_dict.clear()
print(my_dict)

# Dictionary Methods
# Here are some commonly used dictionary methods:

# 1. keys()
# Returns a view of all keys in the dictionary.
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
keys = my_dict.keys()  # dict_keys(["name", "age", "city"])
print(keys)

# 2. values()
# Returns a view of all values in the dictionary.
values = my_dict.values()  # dict_values(["Alice", 25, "New York"])
print(values)

# 3. items()
# Returns a view of all key-value pairs as tuples.

items = my_dict.items()  # dict_items([("name", "Alice"), ("age", 25), ("city", "New York")])
print(items)

# 4. update()
# Updates the dictionary with key-value pairs from another dictionary or iterable.

my_dict.update({"age":26,"Country":"USA"})
print(my_dict)

# 5. copy()
# Returns a shallow copy of the dictionary.

new_dict = my_dict.copy()
print(new_dict)

# 6. fromkeys(keys, value)
# Creates a new dictionary with the specified keys and a default value.

keys=["a","b","c"]
default_dict=dict.fromkeys(keys,0) # {"a": 0, "b": 0, "c": 0}
print(default_dict)

# Iterating Over a Dictionary
# You can iterate over keys, values, or key-value pairs.

# Iterating over keys
for key in my_dict.keys():
    print(key)

# Iterating over values
for value in my_dict.values():
    print(value)

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(key, value)


# Dictionary Comprehension
# Dictionary comprehension allows you to create dictionaries in a concise way.

cubes={x : x**3 for x in range(1,6)}
print(cubes)

# Creating a dictionary
student = {"name": "John", "age": 21, "courses": ["Math", "Science"]}

# Accessing values
print(student["name"])  # Output: John
print(student.get("age"))  # Output: 21

# Adding a new key-value pair
student["grade"] = "A"

# Modifying a value
student["age"] = 22

# Removing a key-value pair
student.pop("grade")

# Iterating over key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")

'''Key Points to Remember
Dictionaries store data in key-value pairs.

Keys must be unique and immutable.

Use get() to safely access values without raising a KeyError.

Dictionaries are mutable and optimized for fast lookups.

Use dictionary comprehension for concise dictionary creation.
'''



