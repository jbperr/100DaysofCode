import Day14_game_data as dt
import random
import HighLowArt as art
import os


def generate(points):
    ranA = random.choice(dt.data)
    ranB = random.choice(dt.data)
    ranAfoll = ranA["follower_count"]
    ranBfoll = ranB["follower_count"]
    os.system("clear")
    print(art.logo)
    if points > 0:
        print(f"You're right! Current score: {points}")
    print(f'Compare A: {ranA["name"]}, a {ranA["description"]}, from {ranA["country"]}')
    print(art.vs)
    print(f'Compare B: {ranB["name"]}, a {ranB["description"]}, from {ranB["country"]}')
    guess = input("Who has more followers? Type (A) or (B): ")
    result(userGuess=guess, aFoll=ranAfoll, bFoll=ranBfoll, scr=points)


def result(userGuess, aFoll, bFoll, scr):
    bigFol = "A"
    if aFoll < bFoll:
        bigFol = "B"
    if userGuess == bigFol:
        scr += 1
        print(scr)
        generate(points=scr)
    else:
        os.system("clear")
        print(art.logo)
        print(f"Sorry, thats wrong. Final score: {scr}")


generate(points=0)
