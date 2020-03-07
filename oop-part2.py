# 4 pillars of OOP

# 1 Encapsulation - group everything related in a sel containing unit or class/

# 2 Abstraction - To hide away things / details we dont need to know to use methods on a object
# Just remember there is no such thing as private variables, one could 'cheat' and mangle your variables with a _,
# but that wont totally protect your variables

# 3 - Inheritance
class User:
    def sign_in(self):
        print("logged in")


class Wizard(User):
    def __init__(self, name, power):
        # super().__init__(
        #     email
        # )  # we need to do this if we want to include the init function from base class
        self.name = name
        self.power = power

    def attack(self):
        print(f"{self.name} attacking with power {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"{self.name } has {self.num_arrows} arrows in his quiver")

    def run(self):
        print("run very fast")


# Be vey careful when dealing with multiple inheritance, it is very tricky when dealing with those parameters in each other class
class MageHunter(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Archer.__init__(self, name, num_arrows)
        Wizard.__init__(self, name, power)


mh1 = MageHunter("Rufud", 60, 50)
print(mh1.run())


wizard1 = Wizard("Raistlin", 90)
archer1 = Archer("Reggie", 100)
archer1.sign_in()
archer1.attack()
print(dir(archer1))
print(isinstance(archer1, Archer))  # true
print(isinstance(archer1, User))  # True
print(
    isinstance(archer1, object)
)  # just keep in mind there is a chain of inheritance, so archer1 will have access to the base class of object
# archer1 << Archer << User << object - again similiar to JavaScript and its chain to the Prototype

# 4 Polymorphism - doing something different depending on the class / object on the same function call, see below

for character in [wizard1, archer1]:
    character.attack()

# Dunder / Magic Methods - allows us to use Python specific functions in our class,
class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            "name": "Yoyo",
            "has_pets": False,
        }

    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return 5

    def __del__(self):
        return "deleted"

    def __call__(self):
        return "yes??"

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy("red", 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure["name"])

# Exercise 1
class SuperList(list):  # inheriting from base List
    def __len__(self):
        return 1000


super_list1 = SuperList()

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(list, object))
