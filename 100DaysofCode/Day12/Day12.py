import random
import numguessart

def guess(user, rand, difficulty):
    if difficulty == 'easy':
        lives = 10
    elif difficulty == 'hard':
        lives = 5
    win = False
    while lives > 0 or win == False:
        if user == rand:
            win = True
            print(f'Correct! The number was {rand}')
            break
        elif user > rand:
            print('Too high')
            lives -= 1
        elif user < rand:
            print('Too low')
            lives -= 1
        if lives == 0:
            print('You have no tries left.')
            break
        print(f'You have {lives} tries left')
        user = int(input('Guess again: '))

print(numguessart.logo)
num = random.randint(1,101)
diffi = input('Choose a difficulty. (easy) or (hard)')
user_guess = int(input("Try to guess the number from 0 to 100! "))

guess(user = user_guess, rand = num, difficulty = diffi)