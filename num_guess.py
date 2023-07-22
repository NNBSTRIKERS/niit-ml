import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Select a range for the number to be guessed.")
    lower_limit = int(input("Enter the lower limit: "))
    upper_limit = int(input("Enter the upper limit: "))
    
    # Generate a random number within the selected range
    secret_number = random.randint(lower_limit, upper_limit)
    
    # Initialize variables
    guess = None
    num_guesses = 0
    
    while guess != secret_number:
        guess = int(input("Take a guess: "))
        num_guesses += 1
        
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
    
    print(f"Congratulations! You guessed the number {secret_number} in {num_guesses} guesses.")

# Run the game
number_guessing_game()
