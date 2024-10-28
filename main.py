import random
from hangman_word import word_list
from  hangman_art import logo

lives = 6
print(logo)


chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"you have {lives}/6 LIVES LEFT")
    guess = input("Guess a letter: ").lower()


    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            print(f"you have already guessed this letter {letter}")
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word to guess , you lose a life ")
        if lives == 0:
            game_over = True

            print(f"the correct word is {chosen_word} YOU LOSE")

    if "_" not in display:
        game_over = True
        print("YOU WIN ")

    from hangman_art import stages
    print(stages[lives])
