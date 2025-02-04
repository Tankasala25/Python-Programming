'''Lambda functions in Python are a concise way to create anonymous functions (functions without a name). 
They are often used for short, throwaway functions where defining a full function using def would be unnecessary.
 Let’s dive deep into lambdas, covering their syntax, use cases, limitations, and how they fit into Python’s functional 
programming paradigm.'''

# 1. Syntax of Lambda Functions

# lambda arguments: expression

# lambda: The keyword used to define a lambda function.

# arguments: The input parameters (similar to a regular function).

# expression: A single expression that is evaluated and returned. Lambdas can only contain one expression.

# Regular function
def add(a,b):
    return a+b
# Equivalent lambda function
add_lambda=lambda a,b:a+b

print(add(2,3))
print(add_lambda(2,3))

'''2. Characteristics of Lambda Functions
Anonymous: Lambdas don’t have a name (unless explicitly assigned to a variable).

Single Expression: They can only contain one expression, which is evaluated and returned.

No Statements: Lambdas cannot include statements like if, for, while, or return.

Inline Use: Lambdas are often used inline, where a function is needed for a short period.'''

# 3. Use Cases for Lambda Functions
# a. With map()
# The map() function applies a function to all items in an iterable. Lambdas are often used here for simplicity.

numbers=[1,2,3,4,5]
squared=map(lambda x:x**2,numbers)
print(list(squared))

# b. With filter()
# The filter() function filters items in an iterable based on a condition. Lambdas are commonly used to define the condition.

numbers=[1,2,3,4,5,6]
even_numbers=filter(lambda x:x%2==0,numbers)
print(list(even_numbers))

# c. With sorted()
# The sorted() function sorts an iterable. Lambdas can be used to define custom sorting keys.

students = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
# Sort by age
sorted_students = sorted(students,key=lambda x:x[1])
print(sorted_students) 

# d. With reduce()
# The reduce() function (from the functools module) applies a function cumulatively to items in an iterable. Lambdas are often used here.

from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x,y:x*y,numbers)
print(product)  

# e. Inline Use
# Lambdas are often used inline where a function is needed temporarily.

# Inline lambda
result = (lambda x,y:x+y)(10,20)
print(result)  # Output: 30

'''4. Limitations of Lambda Functions
Single Expression: Lambdas can only contain one expression. If you need multiple statements, use a regular function.

No Statements: Lambdas cannot include statements like if, for, or return. However, you can use conditional expressions (ternary operator).

Readability: Overusing lambdas can make code harder to read. Use them only when they improve clarity.'''

# 5. Advanced Use Cases
# a. Conditional Logic in Lambdas
# You can use the ternary operator (x if condition else y) to include conditional logic in lambdas.
# Lambda with conditional logic
max_value=lambda x,y:x if x>y else y
print(max_value(40,20))

# b. Nested Lambdas
# Lambdas can be nested, but this can reduce readability.

# Nested lambda
func = lambda x: (lambda y: x + y)
result = func(10)(20)
print(result)  

# c. Lambdas with Default Arguments
# Lambdas can have default arguments, just like regular functions.

greet= lambda greet="Guest":f"Hello, {greet}"
print(greet())
print(greet("Raj"))

# 6. Lambdas vs Regular Functions
# Feature->Lambda Functions->	Regular Functions (def)
# Name->	Anonymous (no name unless assigned)->	Named
# Expression/Statements->	Single expression only	->Can contain multiple statements
# Readability->	Less readable for complex logic	->More readable for complex logic
# Use Case->	Short, throwaway functions->	Reusable, complex functions

# 7. Best Practices
# Use Sparingly: Lambdas are great for short, simple operations. Avoid using them for complex logic.

# Improve Readability: If a lambda makes your code harder to read, use a regular function instead.

# Combine with Functional Tools: Lambdas shine when used with map(), filter(), sorted(), and reduce().

# 8. Examples in Real-World Scenarios
# a. Sorting a List of Dictionaries

student=[
    {"name":"Alice","age":25},
    {"name":"Bob","age":20},
    {"name":"Charlie","age":30},
]

sort_students=sorted(student, key=lambda x:x["age"])
print(sort_students)

# b. Filtering a List

numbers=[1,2,3,4,5,6]
even_num=filter(lambda x:x%2==0,numbers)
print(list(even_num))

# c. Mapping with a Condition

numbers=[1,2,3,4]

squared_numbers=map(lambda x:x**2 if x%2==0 else x,numbers)
print(list(squared_numbers))




