def get_letter_guess():
    # TODO: Students to fill in this function
    pass

def play_hangman():
    word = "hangman"  # The word to guess
    guessed_letters = []  # The letters that have been guessed
    attempts = 6  # The number of incorrect guesses the player can make

    while attempts > 0:
        # Print the current state of the guessed word
        print(' '.join(letter if letter in guessed_letters else '_' for letter in word))

        # Get a letter guess from the user
        guess = get_letter_guess()

        if guess in word:
            # If the guess is correct, add it to the list of guessed letters
            guessed_letters.append(guess)
        else:
            # If the guess is incorrect, decrement the number of attempts
            attempts -= 1
            print(f"Incorrect guess. You have {attempts} attempts remaining.")

        # Check if the word has been completely guessed
        if set(guessed_letters) == set(word):
            print("Congratulations, you've guessed the word!")
            return

    print("Sorry, you've run out of attempts. The word was:", word)

play_hangman()
