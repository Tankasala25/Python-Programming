Python provides a wide range of built-in string methods that allow you to manipulate and work with strings efficiently. Below is a comprehensive list of commonly used string methods, along with examples for each.

1. Case Conversion Methods
These methods change the case of the string.

Method	Description	Example
upper()	Converts the string to uppercase.	"hello".upper() → "HELLO"
lower()	Converts the string to lowercase.	"HELLO".lower() → "hello"
title()	Converts the first character of each word to uppercase.	"hello world".title() → "Hello World"
capitalize()	Converts the first character of the string to uppercase.	"hello".capitalize() → "Hello"
swapcase()	Swaps uppercase to lowercase and vice versa.	"Hello World".swapcase() → "hELLO wORLD"
2. Searching and Checking Methods
These methods check for the presence of substrings or specific conditions.

Method	Description	Example
find(sub)	Returns the lowest index of the substring. Returns -1 if not found.	"hello".find("e") → 1
index(sub)	Similar to find(), but raises an error if not found.	"hello".index("e") → 1
rfind(sub)	Returns the highest index of the substring. Returns -1 if not found.	"hello".rfind("l") → 3
rindex(sub)	Similar to rfind(), but raises an error if not found.	"hello".rindex("l") → 3
startswith(prefix)	Checks if the string starts with the given prefix.	"hello".startswith("he") → True
endswith(suffix)	Checks if the string ends with the given suffix.	"hello".endswith("lo") → True
count(sub)	Returns the number of occurrences of a substring.	"hello".count("l") → 2
isalnum()	Checks if all characters are alphanumeric (letters or numbers).	"hello123".isalnum() → True
isalpha()	Checks if all characters are alphabetic.	"hello".isalpha() → True
isdigit()	Checks if all characters are digits.	"123".isdigit() → True
isnumeric()	Checks if all characters are numeric (including Unicode numbers).	"½".isnumeric() → True
isspace()	Checks if all characters are whitespace.	" ".isspace() → True
islower()	Checks if all characters are lowercase.	"hello".islower() → True
isupper()	Checks if all characters are uppercase.	"HELLO".isupper() → True
istitle()	Checks if the string is title-cased.	"Hello World".istitle() → True
3. Formatting Methods
These methods format the string.

Method	Description	Example
strip()	Removes leading and trailing whitespace.	" hello ".strip() → "hello"
lstrip()	Removes leading whitespace.	" hello ".lstrip() → "hello "
rstrip()	Removes trailing whitespace.	" hello ".rstrip() → " hello"
replace(old, new)	Replaces occurrences of old with new.	"hello".replace("l", "x") → "hexxo"
zfill(width)	Pads the string with zeros on the left.	"42".zfill(5) → "00042"
center(width)	Centers the string in a field of given width.	"hello".center(10) → " hello "
ljust(width)	Left-justifies the string in a field of given width.	"hello".ljust(10) → "hello "
rjust(width)	Right-justifies the string in a field of given width.	"hello".rjust(10) → " hello"
4. Splitting and Joining Methods
These methods split or join strings.

Method	Description	Example
split(sep)	Splits the string into a list using sep as the delimiter.	"hello world".split() → ["hello", "world"]
rsplit(sep)	Splits the string from the right.	"hello world".rsplit() → ["hello", "world"]
splitlines()	Splits the string at line breaks.	"hello\nworld".splitlines() → ["hello", "world"]
join(iterable)	Joins elements of an iterable into a string.	" ".join(["hello", "world"]) → "hello world"
5. Character Encoding Methods
These methods handle character encoding.

Method	Description	Example
encode(encoding)	Encodes the string into bytes.	"hello".encode("utf-8") → b'hello'
decode(encoding)	Decodes bytes into a string.	b'hello'.decode("utf-8") → "hello"
6. Other Useful Methods
Method	Description	Example
format()	Formats the string using placeholders.	"{} world".format("hello") → "hello world"
format_map(mapping)	Formats the string using a mapping.	"{name} world".format_map({"name": "hello"}) → "hello world"
expandtabs(tabsize)	Replaces tabs with spaces.	"hello\tworld".expandtabs(4) → "hello world"
partition(sep)	Splits the string into three parts (before, sep, after).	"hello world".partition(" ") → ("hello", " ", "world")
rpartition(sep)	Similar to partition(), but searches from the right.	"hello world".rpartition(" ") → ("hello", " ", "world")
