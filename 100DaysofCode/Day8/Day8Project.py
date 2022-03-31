import cipher_art

print(cipher_art.logo)

alphabet = [
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
]
should_continue = True


def caesar(d, t, s):
    if s >= 26:
        s = s % 26
    cipher = ""
    for i in text:
        if i in alphabet:
            position = alphabet.index(i)
            if direction == "encode":
                new_position = position + s
            elif direction == "decode":
                new_position = position - s
            else:
                print("Wrong input")
                return
            new_letter = alphabet[new_position]
            cipher += new_letter
        else:
            cipher += i
    print(cipher)


while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(d=direction, t=text, s=shift)
    cont = input("Keep going? (yes/no)")
    if cont == "no":
        should_continue = False
