is_old = True
is_licensed = True

if is_old and is_licensed:
    print("You are old enough to drive")
# elif is_licensed:
#     print("You can drive")
else:
    print("You are to young to drive")


# truthy and falsy
username = "test"  # considered truthy can be used in an if statement. Almost anything with a value is considered Truthy, ecept 0 of course
password = 123  # considered truthy can be used in an if statement
test = ""  # Considered falsy, there are others like 0, None etc that are also falsy

if username:
    print("it is truthy")
else:
    print("Falsy")

if test:
    print("it is truthy")
else:
    print("Falsy")

# Ternary operator

# condition_if_true if condition else condition_if_else
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)

# Short Circuiting

friend_status = True
is_user = True

if friend_status or is_user:
    print("best buds")

# logical operators
print(10 > 5)
print(10 < 25)
print(10 <= 5)
print(0 != 4)
print(not (3 == 5))

# Exercise 1
is_wizard = True
is_expert = False

if is_wizard and is_expert:
    print("You are a master magician")
elif is_wizard and not is_expert:
    print("at least you are getting there")
elif not is_wizard:
    print("You need magic powers")

# is - a stricter form of evaluation, is checks the memory loacation not the value so
print(10 is 10)  # true - the same simple variable is stored at the same location
print(10 is 9)  # false
print(
    [] is []
)  # false, complex data structures are always created at a different memory location
print({} is {})  # false - same as above

