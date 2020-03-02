# Fundamental Data types
int
float
bool
str
list
tuple
set
dict

# Classes - custom data type

# Specialized data types - external packages

None

# int and float
print(type(3 + 3))
print(type(2 * 8))
print(type(2 / 8))

print(2 ** 2)  # 4
print(4 // 2)  # rounds down to integer
print(6 % 4)  # modular remainder

# Math fnctions
print(round(10.5))
print(round(10.6))
print(round(11.2))

print(abs(-200))  # 200
print(bin(8))  # 0b1000 - prints binary
print(int("0b1000", 2))  # 8

# Variables
user_iq = 150  # snake case, must start with underscore or letter, case sensitive

a, b, c, d = 5, 10, 15, 20  # to assign multiple variables at once

# constants
PI = 3.141

# Expression + Statement
user_age = user_iq / 5  # user_iq / 5 is an expression, whole line is a statement

# Augmented Assignment Operator, like i++ in loops
some_num = 5
some_num += 10
print(some_num)
