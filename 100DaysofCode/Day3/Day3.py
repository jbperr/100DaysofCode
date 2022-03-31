# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# price = 0
# if height >= 120:
    # print("You can ride the rollercoaster")
    # age = int(input("What is your age? "))
#
    # if age < 12:
        # price = 5
        # print("child tickets are $5.")
    # elif age <= 18:
        # price = 7
        # print("Youth tickets are $7")
    # elif age >= 45 and age <= 55:
        # price = 0
        # print("It's on the House")
    # else:
        # price = 12
        # print("Adult tickets are $12")
#
    # photo = input("Do you want a photo taken? Y or N ")
    # if photo == "Y" or photo == "y":
        # price += 3
    # print(f"Your final price is {price}")
# else:
    # print("You can't ride the rollercoaster")

#===========================================#

# number = int(input("Which number do you want to check? "))
#
# if number % 2 == 0:
    # print(f"{number} is even")
# else:
    # print(f"{number} is odd")
#====================================================#
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
#
# bmi = round(weight / (height ** 2))
#
# if bmi < 18.5:
    # print(f"Your BMI is {bmi} and you are underweight")
# elif bmi < 25:
    # print(f"Your BMI is {bmi} and you are a normal weight")
# elif bmi < 30:
    # print(f"Your BMI is {bmi} and you are overweight")
# elif bmi < 35:
    # print(f"Your BMI is {bmi} and you are obese")
# else:
    # print(f"Your BMI is {bmi} and you are clinically obese")

#=========================================#

# year = int(input("Which year do you want to check? "))
#
# if year % 4 == 0:
    # if year % 100 == 0:
        # if year % 400 == 0:
            # print("Leap year.")
        # else:
            # print("Not leap year.")
    # else:
        # print("Leap year.")
# else:
    # print("Not leap year.")
#=========================================#
#
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill = 0
#
# if extra_cheese == "y":
    # bill += 1
#
# if size == "s":
    # bill += 15
    # if add_pepperoni == "y":
        # bill+=2
# elif size == "m":
    # bill += 20
    # if add_pepperoni == "y":
        # bill += 3
# elif size == "l":
    # bill += 25
    # if add_pepperoni == "y":
        # bill += 3
# print(f"Your bill is ${bill}")

#======================================#
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combineName = (name1 + name2).lower()

T = combineName.count('t')
R = combineName.count('r')
U = combineName.count('u')
E = combineName.count('e')
L = combineName.count('l')
O = combineName.count('o')
V = combineName.count('v')

addTrue = T + R + U + E
addLove = L + O + V + E

combineScore = str(addTrue) + str(addLove)
score = int(combineScore)

if (score < 10) or (score >= 90):
    print(f"Your score is {score} you go together like coke and mentos")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score} you are alright together.")
else:
    print(f"Your score is {score}")
