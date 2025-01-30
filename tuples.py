'''In Python, a tuple is an ordered, immutable collection of elements. Once a tuple is created, its contents cannot be changed 
(i.e., you cannot add, remove, or modify elements). Tuples are similar to lists, but they are more memory-efficient and faster for 
fixed data. They are commonly used for storing related pieces of information, such as coordinates or database records.

Creating a Tuple
Tuples are created by enclosing elements in parentheses () and separating them with commas. The parentheses are optional, 
but they are often used for clarity.'''

# Creating a tuple
# my_tuple = (1, 2, 3, 4)
another_tuple = 5, 6, 7  # Parentheses are optional

# Single-element tuple (note the trailing comma)
single_element_tuple = (42,)

# Mixed data types
mixed_tuple = (1, "hello", 3.14, True)

# Accessing Tuple Elements
# You can access tuple elements using indexing or slicing, just like lists.

my_tuple =(10, 20, 30, 40)

# Accessing elements
print(my_tuple[0])  # Output: 10
print(my_tuple[-1])  # Output: 40 (last element)

# Slicing
print(my_tuple[1:3])  # Output: (20, 30)

# Tuple Operations
# 1. Concatenation
# You can combine tuples using the + operator.

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2  
print(combined_tuple) # (1, 2, 3, 4, 5, 6)

# 2. Repetition
# You can repeat a tuple using the * operator.

repeated_tuple = tuple1 * 2  
print(repeated_tuple) # (1, 2, 3, 1, 2, 3)

# 3. Membership Testing
# You can check if an element exists in a tuple using the in keyword.

if 2 in tuple1:
    print("2 is in the tuple")

# Tuple Methods
# Since tuples are immutable, they have fewer built-in methods compared to lists. The most commonly used methods are:

# 1. count(x)
# Returns the number of times an element x appears in the tuple.

my_tuple = (1, 2, 2, 3, 2)
print(my_tuple.count(2))  # Output: 3

# 2. index(x)
# Returns the index of the first occurrence of element x. Raises an error if the element is not found.
print(my_tuple.index(3))  # Output: 3

# Unpacking Tuples
# You can unpack a tuple into individual variables.

my_tuple = (10, 20, 30,40)
a, b, c, d = my_tuple
print(a, b, c, d)  # Output: 10 20 30 40

# You can also use the * operator to unpack multiple elements into a single variable.

*a, b = my_tuple
print(a)  # Output: [10,20,30]
print(b)  # Output: 40

# Example: Returning Multiple Values from a Function
# Tuples are often used to return multiple values from a function.

def get_coordinates():
    return (10, 20)

x, y = get_coordinates()
print(x, y)  # Output: 10 20



# Example

# Creating a tuple
coordinates = (3.5, 7.2)

# Accessing elements
print(coordinates[0])  # Output: 3.5

# Unpacking
x, y = coordinates
print(x, y)  # Output: 3.5 7.2

# Concatenation
new_coordinates = coordinates + (5.0,)
print(new_coordinates)  # Output: (3.5, 7.2, 5.0)

# Membership testing
if 7.2 in coordinates:
    print("7.2 is in the tuple")


'''Key Points to Remember
Tuples are immutable, so you cannot modify them after creation.

Use tuples for fixed data and lists for dynamic data.

Tuples are hashable and can be used as dictionary keys.

Use parentheses () to create tuples, but they are optional.'''