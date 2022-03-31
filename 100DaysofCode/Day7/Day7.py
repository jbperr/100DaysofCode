import random
import hangman_art
import hangman_words

stages = hangman_art.stages
word_list = hangman_words.word_list
chosenWord = random.choice((word_list))
end_of_game = False
lives = 6
display = ["_"] * len(chosenWord)
prevGuess = []

print(hangman_art.logo)

while not end_of_game:
    print(stages[lives])
    guess = input("Guess a letter: ").lower()

    if guess in prevGuess:
        print(f"You've already guessed {guess}")
        lives += 1

    prevGuess.append(guess)

    for i in range(len(chosenWord)):
        if guess == chosenWord[i]:
            display[i] = guess

    if guess not in chosenWord:
        print(f"{guess} is not in the word")
        lives -= 1

    print(f"{' '.join(display)}")

    if lives == 0:
        end_of_game = True
        print(stages[lives])
        print(chosenWord)
        print("you lose")
    if "_" not in display:
        end_of_game = True
        print(stages[lives])
        print("You win!")
