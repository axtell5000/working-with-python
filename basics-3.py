# boolean
is_cool = True

print(bool(1))
print(bool(0))
print(type(bool("True")))

# Exercise
birth_year = input("What year where you born? ")
age = 2020 - int(birth_year)
print(type(age))
print(f"You are {age} years old")

# Exercise 2
username = input("Please enter your username ")
password = input("Please enter your password ")
password_length = len(password)
stars_string = password_length * "*"

print(password)
print(password_length)
print(
    f"Hello {username}, your password {stars_string} is {password_length} letters long"
)

