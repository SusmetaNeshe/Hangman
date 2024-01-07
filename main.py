import random

def choose_word():
    words = ["chocolate", "cake", "candy", "love", "Dress", "cookies", "sweet"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 10

    print("Welcome to Hangman!")
    while True:
        print(display_word(word, guessed_letters))
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter or the full word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter!")
            elif guess in word:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Oops! That letter is not in the word.")
                attempts -= 1
        elif len(guess) == len(word) and guess.isalpha():
            if guess == word:
                print("Congratulations! You guessed the word!")
                break
            else:
                print("Sorry, that's not the word.")
                attempts -= 1
        else:
            print("Invalid input. Please enter a single letter or the full word.")

        if attempts == 0:
            print("You're out of attempts! The word was:", word)
            break

        if all(letter in guessed_letters for letter in word):
            print("Congratulations!!! You guessed the word:", word)
            break

if __name__ == "__main__":
    hangman()
