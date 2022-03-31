import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]  # 52
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]  # 10
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]  # 9

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

passwordlist = []
# START WITH 6 LONG JUST letters
for i in range(1, nr_letters + 1):
    randlett = random.randint(0, len(letters) - 1)
    passwordlist.append(letters[randlett])
for i in range(1, nr_symbols + 1):
    randsymb = random.randint(0, len(symbols) - 1)
    passwordlist.append(symbols[randsymb])
for i in range(1, nr_numbers + 1):
    randnumb = random.randint(0, len(numbers) - 1)
    passwordlist.append(numbers[randnumb])

random.shuffle(passwordlist)

password = "".join(passwordlist)
print(password)
