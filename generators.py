# Generators - generates iterable values one at a time


def generator_function(num):
    for i in range(num):
        yield i


g = generator_function(100)

print(next(g))
print(next(g))
print(next(g))

from time import time


def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f"took {t2-t1} s")
        return result

    return wrapper


@performance
def long_time():
    print("1")
    for i in range(100000):
        i * 5


@performance
def long_time2():
    print("2")
    for i in list(range(100000)):
        i * 5


long_time()
long_time2()

# Exercise
def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fib(21):
    print(x)

