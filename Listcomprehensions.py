# List Comprehensions
# List comprehensions provide a compact way to create lists. They are often more readable and faster than using loops.

# [expression for item in iterable if condition]

# expression: The value to include in the new list.

# item: The variable representing each element in the iterable.

# iterable: The collection you're iterating over (e.g., list, range, tuple).

# condition (optional): Filters items to include only those that satisfy the condition.

# 1. Basic List Comprehension
# Create a list of squares of numbers from 1 to 10.

squares=[x**2 for x in range(1,11)]
print(squares)

# 2. List Comprehension with Condition
# Create a list of even numbers from 1 to 20.

even_numbers=[x for x in range(1,21) if x%2==0]
print(even_numbers)

# 3. Nested List Comprehension
# Create a flattened list from a 2D list.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 4. List Comprehension with Function
# Apply a function to each element in a list.

words = ["hello", "world", "python"]
lengths=[len(word) for word in words]
print(lengths)

text="Hello World"
characters=[character.upper() for character in text if not character==" " ]
print(characters)

# Combining List and Dictionary Comprehensions
# You can combine list and dictionary comprehensions to create more complex data structures.

# Example: List of Dictionaries
# Create a list of dictionaries where each dictionary contains a number and its square.
squares_list=[{x:x**2} for x in range(1,6)]
print(squares_list)