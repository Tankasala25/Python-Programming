'''In Python, a list is a versatile and widely used data structure that allows you to store an ordered collection of items. 
Lists are mutable, meaning you can modify their contents after creation. Lists can contain elements of different data types, 
including integers, strings, floats, and even other lists.

Creating a List
You can create a list by enclosing elements in square brackets [], separated by commas.'''

my_list = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]

# 1. Adding Elements

# append(x): Adds an element x to the end of the list.

my_list.append(6)  # [1, 2, 3, 4, 5, 6]
print(my_list)

# extend(iterable): Adds all elements from an iterable (e.g., list, tuple) to the end of the list.

my_list.extend([7,8])
print(my_list)

# insert(i, x): Inserts an element x at a specific index i.

my_list.insert(2,99)
print(my_list)

# 2. Removing Elements
# remove(x): Removes the first occurrence of element x from the list. Raises an error if the element is not found.

my_list.remove(99)
print(my_list)

# pop([i]): Removes and returns the element at index i. If no index is specified, it removes and returns the last element.
my_list.pop(1) #delete index 1
my_list.pop() #removes last element
# mylist.pop(12)- raises error index out of range error
print(my_list)

# clear(): Removes all elements from the list, making it empty.
my_list.clear()
print(my_list)

# 3. Accessing Elements
# index(x): Returns the index of the first occurrence of element x. Raises an error if the element is not found.
my_list = [1, 6, 3, 4, 5,2]
print(my_list.index(4))

# count(x): Returns the number of times element x appears in the list.
print(my_list.count(2))

# 4. Sorting and Reversing
# sort(key=None, reverse=False): Sorts the list in place. You can specify a key function for custom sorting and reverse=True for descending order.

# my_list.sort()
# print(my_list)

# my_list.sort(reverse=True)
# print(my_list)

my_list.reverse()
print(my_list)

# 5. Copying Lists
# copy(): Returns a shallow copy of the list.
newlist=my_list.copy()
print(newlist)

new_list=my_list[:]
print(new_list)

# 6. Other Useful Methods
# len(list): Returns the number of elements in the list.

print(len(my_list))

# in operator: Checks if an element exists in the list.

if 3 in my_list:
    print("3 is in the list")

# + operator: Concatenates two lists.
combined_list = my_list + [9, 10]
print(combined_list)

# * operator: Repeats a list.

repeated_list = my_list * 2
print(repeated_list)


# Create a list
fruits = ["apple", "banana", "cherry"]

# Add elements
fruits.append("orange")
print(fruits)
fruits.insert(1, "mango")
print(fruits)
# Remove elements
fruits.remove("banana")
print(fruits)
fruits.pop()
print(fruits)
# Sort and reverse
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
# Access elements
print(fruits[0])  # Output: mango
print(fruits.index("cherry"))  # Output: 1

# Copy the list
new_fruits = fruits.copy()

# Print the final list
print(new_fruits)  # Output: ['mango', 'cherry', 'apple']