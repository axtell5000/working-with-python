# Pure functions
from functools import reduce  # importing a package


def multiply_by_3(li):
    new_list = []
    for item in li:
        new_list.append(item * 3)
    return new_list


print(multiply_by_3([10, 20, 30]))
# THe above is a pure function because 1) if we give it the same parameters it will always give the same reult
# 2 - There is no side effects, if we put the print inside the function that it wont be pure or if it references some global variable

# Filter ,zip()
a_list = [1, 2, 3, 4, 5, 6, 7]
b_list = [10, 20, 30, 49, 50, 60, 70]


def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, a_list)))
print(
    list(zip(a_list, b_list))
)  # Combines a list of iterables, returns list of tuples, one from each list
print(a_list)


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(
    reduce(accumulator, b_list, 0)
)  # like the JavaScript - reducer, takes function, a list of items, initial value
print(b_list)

# Exercises
# 1 Capitalize all of the pet names and print the list
my_pets = ["sisi", "bibi", "titi", "carla"]


def capitalize(string):
    return string.upper()


print(list(map(capitalize, my_pets)))


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ["a", "b", "c", "d", "e"]
my_numbers = [5, 4, 3, 2, 1]

print(list(zip(my_strings, sorted(my_numbers))))


# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def is_smart_student(score):
    return score > 50


print(list(filter(is_smart_student, scores)))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, (my_numbers + scores)))
