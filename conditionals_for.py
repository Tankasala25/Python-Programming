'''A for loop in Python is used to iterate over 
a sequence (such as a list, tuple, dictionary, set, or string) or other iterable objects. The basic syntax of a for loop is:'''
# for item in iterable:
#     # Code to execute for each item
# Here’s a breakdown of how it works:

# item is a variable that takes the value of each element in the iterable, one at a time.

# iterable is the collection of items you want to loop over.

# The code block under the for loop is executed once for each item in the iterable.

# Looping through a list:

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Looping through a string:
for char in "Python":
    print(char)

# Using range() to loop a specific number of times:
for i in range(5):  # Loops from 0 to 4
    print(i)

# Looping through a dictionary:
person = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

# Nested for loops:
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

'''Additional Notes:
You can use break to exit the loop prematurely.

Use continue to skip the rest of the code in the current iteration and move to the next iteration.

The else block can be used with a for loop to execute code after the loop finishes (if it doesn’t encounter a break).

Example with else:'''

for i in range(3):
    print(i)
else:
    print("Loop finished!")


for i in range(4):
    if i==3:
        print(i)
        break
else:
    print('Loop finished')