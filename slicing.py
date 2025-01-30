my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get elements from index 2 to 5 (exclusive)
print(my_list[2:5])  # Output: [2, 3, 4]

# Get elements from the beginning to index 5 (exclusive)
print(my_list[:5])  # Output: [0, 1, 2, 3, 4]

# Get elements from index 5 to the end
print(my_list[5:])  # Output: [5, 6, 7, 8, 9]

# Get every second element
print(my_list[::2])  # Output: [0, 2, 4, 6, 8]

# Reverse the list
print(my_list[::-1])  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

my_string = "Hello, World!"

# Get characters from index 7 to 12 (exclusive)
print(my_string[7:12])  # Output: "World"

# Get the first 5 characters
print(my_string[:5])  # Output: "Hello"

# Get every second character
print(my_string[::2])  # Output: "Hlo ol!"

# Reverse the string
print(my_string[::-1])  # Output: "!dlroW ,olleH"

my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Get elements from index 3 to 7 (exclusive)
print(my_tuple[3:7])  # Output: (3, 4, 5, 6)

# Get every third element
print(my_tuple[::3])  # Output: (0, 3, 6, 9)



# Get the last 3 elements
print(my_list[-3:])  # Output: [7, 8, 9]

# Get elements from index -5 to -2 (exclusive)
print(my_list[-5:-2])  # Output: [5, 6, 7]


# Get every second element starting from index 1
print(my_list[1::2])  # Output: [1, 3, 5, 7, 9]

# Reverse the list with a step of 2
print(my_list[::-2])  # Output: [9, 7, 5, 3, 1]