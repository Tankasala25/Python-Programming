# 1. Square Numbers
# Write a lambda function to square a list of numbers using map().
numbers=[1,2,3,4,5]

squared_numbers=map(lambda x:x**2,numbers)
print(list(squared_numbers))




# 2. Filter Even Numbers
# Write a lambda function to filter out even numbers from a list using filter().

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers=filter(lambda x: x%2==0,numbers)
print(list(filtered_numbers))

# 3. Sort by Length
# Use a lambda function to sort a list of strings by their length.
words = ["apple", "banana", "cherry", "date", "elderberry"]
sorted_words=sorted(words,key=lambda x:len(x))
print(sorted_words)

# 4. Add Two Numbers
# Write a lambda function to add two numbers.

# Your code here
add = lambda x, y: x+y
print(add(10, 20))

# Intermediate Assignments
# 5. Find Maximum Number
# Write a lambda function to find the maximum of two numbers.

# Your code here
max_num = lambda x, y: x if x>y else y
print(max_num(15, 10))

# 6. Check Palindrome
# Write a lambda function to check if a string is a palindrome.

# Your code here
import re
is_palindrome = lambda s:re.sub(r'[^a-zA-Z0-9]', '', s.lower())[::-1] == re.sub(r'[^a-zA-Z0-9]', '', s.lower())
print(is_palindrome("Madam"))  
print(is_palindrome("hello")) 

# 7. Sort List of Tuples
# Sort a list of tuples based on the second element using a lambda function.

data = [(1, 3), (4, 1), (2, 2), (5, 4)]
sorted_data= sorted(data, key=lambda x:x[1])
print(sorted_data)

# 8. Multiply Elements
# Use reduce() and a lambda function to multiply all elements in a list.

from functools import reduce
numbers = [1, 2, 3, 4]
mul_num=reduce(lambda x,y:x*y,numbers)
print(mul_num)

# Advanced Assignments
# 9. Nested Lambdas
# Write a nested lambda function to calculate the sum of three numbers.

# Your code here
add_three = lambda x: lambda y: lambda z: (x+y+z)
print(add_three(10)(20)(30))

# 10. Conditional Mapping
# Use map() and a lambda function to convert a list of numbers into "Even" or "Odd".

numbers = [1, 2, 3, 4, 5]
even_or_odd=map(lambda x: "even" if x%2==0 else "Odd",numbers)
print(list(even_or_odd))


# 11. Filter Strings by Length
# Write a lambda function to filter out strings with a length greater than 5.

words = ["apple", "banana", "cherry", "date", "elderberry"]
words_greater_five=filter(lambda x:len(x)<=5,words)
print(list(words_greater_five))

# 12. Sort Dictionary by Value
# Sort a dictionary by its values using a lambda function.

data = {"apple": 3, "banana": 1, "cherry": 2}
sorted_data= {k:data[k] for k in sorted(data,key=lambda x:x[1]) }
print(sorted_data)

# 13. Custom Key Sorting
# Sort a list of dictionaries by a custom key using a lambda function.

students = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 30}
]
sorted_student=sorted(students,key=lambda x:x["age"])
print(sorted_student)

# 14. Lambda with Default Argument
# Write a lambda function with a default argument to greet a user.

greet = lambda name="Guest": f"Hello, {name}"
print(greet())          
print(greet("Alice"))   

# 15. Lambda in List Comprehension
# Use a lambda function inside a list comprehension to square numbers.

numbers = [1, 2, 3, 4, 5]
squared=map(lambda x:x**2,numbers)
print(list(squared))



# Challenging Assignments
# 16. Factorial Using Lambda and Reduce
# Write a lambda function to calculate the factorial of a number using reduce().

from functools import reduce

factorial=lambda n: reduce(lambda x,y:x*y,range(1,n+1))
print(factorial(5))


# 17. Prime Number Check
# Write a lambda function to check if a number is prime.

# Your code here
import math
is_prime = lambda n:n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1)) 
print(is_prime(7))  # True
print(is_prime(10)) # False