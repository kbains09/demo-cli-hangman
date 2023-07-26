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

