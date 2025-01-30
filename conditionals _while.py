# The while loop in Python is used to repeatedly execute a block of code as long as a given condition is True. It is useful when you don't know in advance how many times the loop needs to run.

# Syntax of while Loop


# while condition:
#    Code to execute as long as the condition is True

''' 
Key Points
The condition is checked before each iteration.

If the condition is False initially, the loop body will never execute.

Be careful to avoid infinite loops (where the condition never becomes False).'''


count = 0

while count < 5:
    print(f"Count is {count}")
    count += 1  # Increment count to avoid an infinite loop


# Example 2: Infinite Loop (and How to Avoid It)

# Infinite loop (don't run this!)
# while True:
#     print("This will run forever!")

count = 0

while True:
    print(f"Count is {count}")
    count += 1
    if count >= 5:
        break  # Exit the loop

# Using else with while Loop
# The else block in a while loop executes when the condition becomes False. It does not execute if the loop is terminated by a break statement.

count = 0

while count < 5:
    print(f"Count is {count}")
    count += 1
else:
    print("Loop finished!")


count=0
while True:
    print(f"count is {count}")
    count+=1
    if count>=5:
        break
else:
    print("loop finished")


# break and continue
# break: Exits the loop immediately.

# continue: Skips the rest of the code in the current iteration and moves to the next iteration.

count=0
while count<10:
    count+=1
    if count==3:
        continue
    if count==7:
        break
    print(f"count is {count}")


#Real World - user validation:

while True:
    user_input=input("please enter the number between 1 and 10:")
    if user_input.isdigit():
        number=int(user_input)
        if 1<=number<=10:
            print(f"Number is {number}")
            break
        else:
            print("Number must be in between 1 and 10")
    else:
        print("Invalid input. Please enter a number.")

# Example 6: Nested while Loops
# You can nest while loops inside other while loops.

i = 1
while i <= 5:  # Outer loop for rows
    j = 1
    while j <= i:  # Inner loop for columns
        print("*", end="")
        j += 1
    print()  # Move to the next line
    i += 1


