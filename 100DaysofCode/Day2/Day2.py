#test = float(2)
#print(type(test))
#====================#
# two_digit_number = input("Type a two digit number: ")

# num1 = int(two_digit_number[0])
# num2 = int(two_digit_number[1])
# sum = num1 + num2

# print(sum)
#======================#
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")

# hint = float(height)
# wint = float(weight)

# bmi = wint / (hint ** 2)

# print(int(bmi))
#=====================#
# score = 0
# score += 1
# print(score)
#=======================#
# age = input("What is your current age? ")
#
# years = 90 - int(age)
# weeks = years * 52
# months = years * 12
# days = years * 365
#
# print(f"You have {days} days, {weeks} weeks, and {months} months left")
#===========================#
bill = float(input("How much was the bill? "))
tip = float(input("What do you want to tip? "))
people = int(input("How many people are splitting? "))

total = bill * (1+(tip/100))
split = round(total / people, 2)

print(f"Each person should pay ${split}.")
