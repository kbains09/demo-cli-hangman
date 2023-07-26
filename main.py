import random

#list of words for the hangman game.
word_list = ["hangman", "python", "programming", "computer", "code", "game", "learning", "challenge"]

def choose_random_word():
    #This function will return a random word from the word_list.
    word = random.choice(word_list)
    return word

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "-"
    return display

def hangman():
    max_attempts = 6
    guessed_letters = []
    word = choose_random_word()
    attempts = 0

    print("Welcome to Hangman!")

    while True:
        print("\nAttempts left: ", max_attempts - attempts)
        print("Guessed letters: ", "".join(guessed_letters))
        print(display_word(word, guessed_letters))

        if "-" not in display_word(word, guessed_letters):
            print("You win!", word)
            break

        if attempts == max_attempts:
            print("You lose!", word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1: or not guess.isalpha():
            print("Invalid input. Try a single letter.")
            continue
    
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts += 1
            print("incorrect guess.")

if__name__ == "__main__":
    hangman()

