# Lamda expressions - an anonymous function that gets run once

some_list = [10, 20, 30, 40, 50, 60]

print(list(map(lambda item: item * 3, some_list)))
print(some_list)

tobe_square = [5, 10, 15, 20]
print(list(map(lambda item: item ** 2, tobe_square)))

nums = [(1, 3), (2, 0), (4, 88), (10, -9)]
nums.sort(
    key=lambda x: x[1]
)  # setting up key attribute so the sort is based on the second value in each tuple
print(nums)

# Comprehensions - allows creating certain data structures quicker - list, set and dictionary

# List
super_list = [char for char in "Shazam"]
super_nums = [num for num in range(0, 50)]
super_nums2 = [num * 3 for num in range(0, 50)]
super_nums3 = [num * 3 for num in range(0, 50) if num % 2 != 0]
print(super_list)
print(super_nums)
print(super_nums2)
print(super_nums3)

# Set
super_list_set = {char for char in "Shazam"}
super_nums_set = {num for num in range(0, 50)}
print(super_list_set)
print(super_nums_set)

# Dictionary
simple_dict = {"a": 1, "b": 2, "c": 10}
another_dict = [1, 2, 3]

my_dict = {key: value ** 2 for key, value in simple_dict.items()}
print(my_dict)

my_dict2 = {num: num * 2 for num in another_dict}
print(my_dict2)

# Exercise
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates)
