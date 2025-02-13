'''Regex (regular expressions) in Python is implemented using the re module. 
Regular expressions are patterns used to match strings and extract, replace, or validate text.'''

# 1. Basic Usage of the re Module
# Python provides the re module to work with regular expressions.

#import re

# 2. Common Regex Functions
# a) re.match() – Matches at the beginning of the string

import re
pattern=r'Hello'
string='Hello, World!'
match=re.match(pattern,string)
if match:
    print("match found:",match.group())

# b) re.search() – Searches for the pattern anywhere in the string

pattern=r"World" 
string ='Hello, World!'
match=re.match(pattern,string)
if match:
    print("Match found:",match.group())

# 3. re.findall() - Find all occurrences in the string

pattern=r'\d+'
string='order 123 and 456'
match=re.findall(pattern,string)
print(match)

# 4. re.finditer() - Find all matches as an iterator


pattern=r'\d+'
string='order 123 and 456'
matches=re.finditer(pattern,string)
for match in matches:
    print(match.group(), "at index", match.start())


# 5. re.sub() - Replace occurrences

pattern=r"\d+"
replacement="###"
string="Order 123 and 456"
new_string=re.sub(pattern,replacement,string)
print(new_string)

# 6. re.split() - Split string at pattern

pattern=r"\s+"
string1="split the string"
split_string=re.split(pattern,string1)
print(split_string)


# 7. Extracting Emails

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
text = "Contact us at support@example.com or sales@example.org"
emails = re.findall(pattern, text)
print(emails)  # Output: ['support@example.com', 'sales@example.org']
