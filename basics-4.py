# lists - in a way similar to arrays

li = [1, 2, 3, 4]
li2 = ["a", "b", "e"]
li3 = [44, "g", False]

amazon_cart = ["tablet", "book", "game", "t-shirt", "shoes"]
print(amazon_cart[0:2])
print(amazon_cart[0::2])

amazon_cart[0] = "ipad"  # lists are mutable
print(amazon_cart[0:3])
print(amazon_cart)  # makes copies
# another_cart = amazon_cart # doing it like this you are copying reference
another_cart = amazon_cart[:]  # this slice / trick allows them to be different
another_cart[0] = "cake"
print(another_cart)
print(amazon_cart)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][1])  # 5

basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]]
print(basket[1][1][0])  # target oranges

# methods
numbers = [2, 4, 6, 8, 10, 12, 1, 0]
print(len(numbers))  # 6

num2 = [[3, 6], [12, 15], [18, 21]]
print(len(num2))  # 3

# append
print(numbers.append(69))  # none, not producing a printable result
print(numbers)  # does what it suppose to

print(numbers.pop(0))  # removes by index
print(numbers)

print(numbers.remove(69))  # removes the actual number 69 in this case
print(numbers)

print(numbers.index(4))  # tells us which index the item appears, here its 0

print(
    6 in numbers
)  # a neater method to avoid those nasty errors. index will thow error if item not found

print(numbers.count(1))  # counts how many times the item appears in the list

numbers.sort()
print(numbers)

print(list(range(1, 25)))  # prints 1 to 24

# list unpacking - like destructuring in JavaScript
a, b, c, *more, d = [10, 20, 30, 40, 50, 60, 70, 80]
print(a)
print(b)
print(c)
print(more)  # prints from 40
print(d)  # print the last item 80
