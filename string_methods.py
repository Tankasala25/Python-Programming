# Case Conversion
print("hello".upper())          # Output: HELLO
print("HELLO".lower())          # Output: hello
print("hello world".title())    # Output: Hello World
print("hello".capitalize())     # Output: Hello
print("Hello World".swapcase()) # Output: hELLO wORLD

# Searching and Checking
print("hello".find("e"))        # Output: 1
print("hello".index("e"))       # Output: 1
print("hello".rfind("l"))       # Output: 3
print("hello".startswith("he")) # Output: True
print("hello".endswith("lo"))   # Output: True
print("hello".count("l"))       # Output: 2
print("hello123".isalnum())     # Output: True
print("hello".isalpha())        # Output: True
print("123".isdigit())          # Output: True
print("½".isnumeric())          # Output: True
print("   ".isspace())          # Output: True
print("hello".islower())        # Output: True
print("HELLO".isupper())        # Output: True
print("Hello World".istitle())  # Output: True

# Formatting
print("  hello  ".strip())      # Output: hello
print("hello".replace("l", "x"))# Output: hexxo
print("42".zfill(5))            # Output: 00042
print("hello".center(10))       # Output:   hello   
print("hello".ljust(10))        # Output: hello     
print("hello".rjust(10))        # Output:      hello

# Splitting and Joining
print("hello world".split())    # Output: ['hello', 'world']
print("hello\nworld".splitlines()) # Output: ['hello', 'world']
print(" ".join(["hello", "world"])) # Output: hello world

# Character Encoding
print("hello".encode("utf-8"))  # Output: b'hello'
print(b'hello'.decode("utf-8")) # Output: hello

# Other Methods
print("{} world".format("hello")) # Output: hello world
print("hello\tworld".expandtabs(4)) # Output: hello   world
print("hello world".partition(" ")) # Output: ('hello', ' ', 'world')