'''In Python, exceptions are events that occur during the execution of a program that disrupt the normal flow of the program's instructions.
When an error occurs, Python generates an exception that can be handled, preventing the program from crashing.

Key Concepts
Exception Handling:

Use try, except, else, and finally blocks to handle exceptions.

The try block contains the code that might raise an exception.

The except block contains the code that executes if an exception occurs.

The else block runs if no exception occurs.

The finally block always executes, regardless of whether an exception occurred.'''

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division successful:", result)
finally:
    print("Execution complete.")


'''Common Built-in Exceptions:

ZeroDivisionError: Division by zero.

TypeError: Operation on an inappropriate type.

ValueError: Function receives an argument of the correct type but inappropriate value.

IndexError: Index out of range.

KeyError: Key not found in dictionary.

FileNotFoundError: File not found.

IOError: Input/Output operation fails.'''

try:
    num = int("abc")
except ValueError:
    print("Invalid integer conversion!")


# Multiple Except Blocks:
# You can handle multiple exceptions by specifying multiple except blocks.

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")


# Catching All Exceptions:
# Use a bare except block to catch all exceptions (not recommended unless necessary).

try:
    risky_operation()
except:
    print("An error occurred!")

# Raising Exceptions:
# Use the raise keyword to manually raise an exception.

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print(age)

try:
    validate_age(-5)
except ValueError as e:
    print(e)  # Output: Age cannot be negative!

# Custom Exceptions:
# You can define custom exceptions by creating a new class that inherits from Python's built-in Exception class.

class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error.")
except CustomError as e:
    print(e)

# Exception Chaining:
# Use raise from to chain exceptions, preserving the original traceback.

# try:
#     10 / 0
# except ZeroDivisionError as e:
#     raise ValueError("Invalid operation") from e

# Finally Block:
# The finally block is used for cleanup actions that must be executed regardless of whether an exception occurred.

try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    if 'file' in locals():
        file.close()
        print("File closed.")

    
# Example: Handling File Operations

# Explanation of the with Statement
# The with statement ensures that the file is properly closed after its suite finishes, even if an exception is raised.

# You don't need to explicitly call file.close() when using with.

try:
    with open("example.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except IOError:
    print("An I/O error occurred!")
else:
    print("File read successfully.")
finally:
    print("Execution complete.")