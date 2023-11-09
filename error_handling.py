def get_letter_guess():
    while True:
        try:
            guess = input("Enter your letter guess: ")
            if not guess.isalpha() or len(guess) != 1:
                raise ValueError
        except ValueError:
            if not guess.isalpha():
                print("Invalid input. Numbers and symbols are not allowed.")
            elif len(guess) != 1:
                print("Invalid input. Please enter only one letter.")
        else:
            return guess.lower()

# Test the function with a variety of inputs
print(get_letter_guess())
