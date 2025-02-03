# Dictionary Comprehensions
# Dictionary comprehensions are similar to list comprehensions but are used to create dictionaries. 
# They allow you to generate key-value pairs in a concise way.

# Syntax
# {key_expression: value_expression for item in iterable if condition}
'''key_expression: The expression to compute the key.

value_expression: The expression to compute the value.

item: The variable representing each element in the iterable.

iterable: The collection you're iterating over.

condition (optional): Filters items to include only those that satisfy the condition.'''

# 1. Basic Dictionary Comprehension
# Create a dictionary of squares for numbers from 1 to 5.

squares={x : x**2 for x in range(1,6)}
print(squares)

# 2. Dictionary Comprehension with Condition
# Create a dictionary of even numbers and their squares.

even_numbers={x:x**2 for x in range(1,11) if x%2==0}
print(even_numbers)


# 3. Dictionary Comprehension with Function
# Create a dictionary where keys are words and values are their lengths.

words = ["apple", "banana", "cherry"]
lengths={word:len(word) for word in words}
print(lengths)

# Swapping Keys and Values
# Swap keys and values in a dictionary.

original_dict = {"a": 1, "b": 2, "c": 3}
new_dict={value:key for key ,value in original_dict.items()}
print(new_dict)

# Example: Dictionary of Lists
# Create a dictionary where keys are numbers and values are lists of their multiples.

multiples = {x: [x * i for i in range(1, 11)] for x in range(1, 3)}
print(multiples)

# Create a frequency dictionary for characters in a string
text = "Largest nation in the world"
frequency = {char:text.count(char) for char in text}
print(frequency)
