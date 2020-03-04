# For loops
for item in "Alien":
    for x in ["a", "b"]:
        print(item, x)

# iterable - list, dictionary, tuple, set, string
# iterate - one by one check eatch item

user = {"name": "Gollum", "age": 300, "can_swim": False}

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

# more complete way
for key, value in user.items():
    print(key, value)

# Exercise 1
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
total = 0

for num in num_list:
    total += num

print(total)

# range - range(start,end(doesnt include this num), step over(default 1))
for number in range(1, 10):
    print(number)

for _ in range(2):
    print(list(range(10)))

# enumerate - only works on iterable objects, returns index as well
for i, char in enumerate(list(range(100))):
    if i == 50:
        print(i, char)

# While loop - be wary of infinite loop
i = 0
while i < 50:
    print(i)
    i += 1
else:
    print("I am done !!")

# Exercise 2
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

for image in picture:
    for pixel in image:
        if pixel:
            print(
                "*", end=""
            )  # end - by fefault it is new line, use end to change that
        else:
            print(" ", end="")
    print("")  # need this for new line

# Exercise 3
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

duplicates = []
for value in some_list:
    if (
        some_list.count(value) > 1
    ):  # count checks how many times a value appears in a list
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

