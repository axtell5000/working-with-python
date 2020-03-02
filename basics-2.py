# Strings
print(type("Super secret dog"))  # str

# 3 '''
long_string_here = """
888
 |
---
"""

print(long_string_here)

first_name = "Stephen"
last_name = "Axtell"
full_name = first_name + " " + last_name
print(full_name)

# Type conversion
a = str(100)
b = int(a)
c = type(b)
print(c)

# Escape sequence, the / allows us to do below
weather = '\t It\'s "kind of" sunny\nHope you have a good day'
print(weather)

# formatted strings - like javascript string literals with the back tick
name = "Big Poppa"
age = 34
print(f"Hi {name}. You are {age} years old")

# string indexes
selfish = "me me and me"
print(selfish[1])  # e

# [start:stop:stepover]
print(selfish[0:5])  # me me
print(selfish[0:6:2])  # m e
print(selfish[::-1])  # -1 reverses from end

# strings are immutable
pet = "Shadow"

# cant do
# pet[3] = "k"

# can only reassign whole string
pet = "Bowzer"

# string built in methods
greet = "howzit"
print(greet[0 : len(greet)])

quote = "i likes to keep it real"
print(quote.upper())
print(quote.capitalize())
print(quote.replace("i", "I"))
