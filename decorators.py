# Decorators - enhancers another function
# In Python functions are first class citizens


def howzit():
    print("Hozit my china")


greet = howzit  # like in JavaScript, one can pass around functions like variables
greet()
del howzit  # When we delete and Python sees us something is referencing that function Python keeps it in memory but deletes the name
greet()
# howzit() wont work

# can pass functions around
def multiHello(func):
    func()
    print("and")
    func()


multiHello(greet)

# Higher Order Function is a function that either receives a function in the parameters or returns a function


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("*******************")
        func(*args, **kwargs)
        print("*******************")

    return wrap_func


@my_decorator
def yelloHello():
    print("Yello")


yelloHello()

# performance decorator.
from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"took {t2-t1}")
        return result

    return wrapper


@performance
def long_time():
    for i in range(10000):
        i * 5


long_time()

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {"name": "Sorna", "valid": True}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]["valid"]:
            return fn(*args, **kwargs)

    return wrapper


@authenticated
def message_friends(user):
    print("message has been sent")


message_friends(user1)
