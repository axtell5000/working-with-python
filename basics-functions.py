# Functions with default parameters
def say_hi(name="Hot Stepper", emoji="8-o"):
    print(f"Hello {name} {emoji}")


# using arguments
say_hi("Stephen", "8-)")

# keyword arguments allows arguments to be in any order
say_hi(emoji="8-(", name="Sad Sack")
say_hi()

# Using return
def add_it_up(num1, num2):
    return num1 + num2


print(add_it_up(12, 13))

# Method must be attached to its owner like a List or String with the . , a function can stand on its own

# Docstrings
def test(a):
    """
	This functions prints the parameter given
	"""
    print(a)


test(7)
help(test)
print(test.__doc__)

# *args and ##kwargs
# args is a tuple
# kwargs - keyword args is a dictionary
# order of parameters is important: params, *args, default params, **kwargs
def new_function(*args, **kwargs):
    print(args, kwargs)


new_function(1, 2, 3, 4, 5, firstname="Stephen", surname="axtell")

# Exercise 1
# def highest_even(li):
#     highest_num = 0
#     for num in li:
#         divisible = num % 2
#         if divisible == 0:
#             if num > highest_num:
#                 highest_num = num
#     print(highest_num)

# or
def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


# highest_even([10, 2, 3, 22, 4, 8, 11, 32])
print(highest_even([10, 2, 3, 22, 4, 8, 11, 32]))

# Scope what vatiable we have access to. Think like old JavaScript where you still have access to variable in loops and if statements
a = 1


def confusion():
    a = 5
    return a


print(a)  # 1
print(confusion())  # 5

# 1 start with local
# 2 parent of local
# 3 Global (no indent)
# 4 built in functions


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
