# def greet():
#     print("He")
#     print("ll")
#     print("o!")

# def greetName(name):
#     print(f"Hello {name}")

# greetName("Ben")

#----------------------#

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"How is it in {location}?")

# greet_with(name = "Ben", location = "Kansas")

#----------------------#
# import random
# import math

# width = random.randint(1,11)
# height = random.randint(1,11)
# coverage = 5

# def numCan(w, h):
#     print(math.ceil((w * h) / coverage))

# numCan(w = width, h = height)

#----------------------#
import random

numb = random.randint(1,200)

def primeCheck(n):
    lst = []
    for i in range(1, n + 1):
        if numb % i == 0:
            lst.append(i)
    if len(lst) == 2:
        print(f"{numb} is prime")
    else:
        print(f"{numb} is not prime")

primeCheck(numb)