class PlayerCharacter:
    # Class Object Attribute
    membership = True  # these are static
    # this is kike a constructor, self is like this in JavaScript
    def __init__(self, name="anonymous", age=10):
        self.name = name
        self.age = age

    def run(self):
        print("run")
        return "done"

    def shout(self):
        print(f"My name is {self.name}")

    @classmethod
    def adding_nums(cls, num1, num2):
        return cls("Dot", num1 + num2)


# @classmethod , allows us to create a method we cann access without instantiating the class
# Same as the Class Object Attribute
print(PlayerCharacter.adding_nums(10, 5))
PlayerCharacter.membership = False
print(PlayerCharacter.membership)

player1 = PlayerCharacter()

print(player1.shout())
print(player1.run())
# help(player1)  # display blueprint of class

player2 = PlayerCharacter("Shazam", 33)
print(player2.shout())

player3 = PlayerCharacter.adding_nums(2, 6)
print(player3.age)

# there is also @ststicmethod - which is similiar to classmethod, but hasnt got access to the class - cls

# Exercise 1
class Cat:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate the Cat object with 3 cats
peanut = Cat("Peanut", 3)
shadow = Cat("Shadow", 5)
snickers = Cat("Snickers", 1)


# Find the oldest cat
def get_oldest_cat(*args):
    return max(args)


# Output
print(
    f"The oldest cat is {get_oldest_cat(peanut.age, shadow.age, snickers.age)} years old."
)

