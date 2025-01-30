# Single-line strings
str1 = 'Hello, World!'
str2 = "Python Programming"

# Multi-line strings
str3 = '''This is a
multi-line string.'''
str4 = """Another way to
write multi-line strings."""

my_string = "Hello"

for char in my_string:
    print(char)

for i in range(len(my_string)):
    print(my_string[i])
 
for i in range(len(my_string)-1,-1,-1):
    print(my_string[i])

for i in my_string[::-1]:
    print(i)

my_string = "Python"
print(my_string[0])  # Output: P
print(my_string[-1]) # Output: n (last character)

str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: Hello World

my_string = "Python Programming"
print("Python" in my_string)  # Output: True
print("Java" in my_string)    # Output: False