# Dictionary in away like object with key / value pairs

dictionary = {"a": 100, "b": 200, "c": 300, "age": 55}

print(dictionary["c"])  # 300

# keyin a dictionary must be unique
print(
    dictionary.get("age")
)  # better way, checks if dictionary has a key of 'age', doesnt throw ugly errors

print(dictionary.get("age", 100))  # setting default value if there is no key - 'age'

print("c" in dictionary)  # true
print(300 in dictionary.keys())  # False, because not in keys
print(300 in dictionary.values())  # true - because there is a value of 300
print(dictionary.items())

# Tuples - like immutable lists
a_tuple = (1, 2, 3, 4, 5, 6, 7, 2)
# a_tuple[0] = 100 this wont work
print(a_tuple.count(2))
print(a_tuple.index(3))

# Set - collection of unordered unique objects
my_set = {1, 2, 3, 4, 5, 6}

my_set2 = {1, 2, 3, 3}
print(my_set2)  # wont print second 3

my_list = ["a", "b", "b", "c", "c", "d"]
print(set(my_list))  # convert a list to a set, remove the duplicates

