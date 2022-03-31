# import random
#
# random_integer = random.randint(1,5)
# print(random_integer)
#
# random_float = random.random()
# print(random_float)
#
# love_score = random.randint(1,100)
# print(love_score)
#====================================#
#
# import random
#
# headsTails = random.randint(0,1)
#
# if headsTails == 1:
    # print("Heads")
# else:
    # print("Tails")
#===================================#
#
# usStates = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
 # "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
 # "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
 # "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
 # "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
 # "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
 # "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
 # "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
 # "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
#=======================================#
# import random
#
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# randomName = random.randint(0,len(names) - 1)
#
# print(f"{names[randomName]} is paying for the bill")
#=========================================#
#       1    2    3
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
#
# horiz = int(position[0])
# vert = int(position[1])
#
# map[vert -1][horiz -1] = "X"
#
# print(f"{row1}\n{row2}\n{row3}")

#========================================#
import random

# rock = "rock"
# paper = "paper"
# scissors = "scissors"

playerChoice = (input("(R)ock (P)aper (S)cissors ")).lower()

#generate computer Choice
genChoice = random.randint(1,3)
compChoice = ""
if genChoice == 1:
    compChoice = "rock"
elif genChoice == 2:
    compChoice = "paper"
elif genChoice == 3:
    compChoice = "scissors"

#game logic
if playerChoice == "r":
    if compChoice == "rock":
        print("Rock. It's a draw")
    elif compChoice == "paper":
        print("Paper. You lose!")
    elif compChoice == "scissors":
        print("Scissors. You win!")
elif playerChoice == "p":
    if compChoice == "rock":
        print("Rock. You win!")
    elif compChoice == "paper":
        print("Paper. It's a draw!")
    elif compChoice == "scissors":
        print("Scissors. I win!")
elif playerChoice == "s":
    if compChoice == "rock":
        print("Rock. I win!")
    elif compChoice == "paper":
        print("Paper. You win!!")
    elif compChoice == "scissors":
        print("Scissors. It's a draw.")
else:
    print("Choose something real!")
