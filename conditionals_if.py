# 1. if Statement
# The if statement is used to execute a block of code only if a condition is true.

x = 10

if x > 5:
    print("x is greater than 5")

# 2. if-else Statement
# The if-else statement is used to execute one block of code if the condition is true and another block if the condition is false.

x = 3

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# 3. if-elif-else Statement
# The if-elif-else statement is used when you have multiple conditions to check. It allows you to test multiple conditions in sequence.

x = 7

if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but less than or equal to 10")
else:
    print("x is 5 or less")

# 4. Nested if Statements
# You can nest if statements inside other if statements to check for more complex conditions.

x = 15

if x > 10:
    print("x is greater than 10")
    if x > 20:
        print("x is also greater than 20")
    else:
        print("x is not greater than 20")
else:
    print("x is 10 or less")

# 5. Ternary Operator (Conditional Expression)
# The ternary operator is a shorthand way to write an if-else statement in a single line.
# syntax-value_if_true if condition else value_if_false

x=7
result="greater than 5" if x>5 else "5 or less"
print(result)


# Logical Operators in Conditionals
# You can combine multiple conditions using logical operators:

# and: True if both conditions are true.

# or: True if at least one condition is true.

# not: Inverts the condition (true becomes false, and vice versa).


x = 7
y = 10

if x > 5 and y > 5:
    print("Both x and y are greater than 5")

if x > 10 or y > 10:
    print("At least one of x or y is greater than 10")

if not x > 10:
    print("x is not greater than 10")


# 7. pass Statement
# The pass statement is a placeholder when you don't want to execute any code in a conditional block. It is often used as a placeholder for future code.

x = 10

if x > 5:
    pass  # Do nothing for now
else:
    print("x is 5 or less")

# 8. Chained Comparisons
# Python allows you to chain multiple comparisons together for cleaner code.

x = 7

if 5 < x < 10:
    print("x is between 5 and 10")