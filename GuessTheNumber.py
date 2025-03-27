import random


def guess_the_number():
    print("\nWelcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess it!\n")

    secret_number = random.randint(1, 100)
    max_attempts = 10
    attempts = 0

    while attempts < max_attempts:
        attempts += 1
        remaining_guesses = max_attempts - attempts + 1

        try:
            guess = int(input(f"Attempt {attempts}/{max_attempts}. Enter your guess: "))

            if guess < secret_number:
                print(f"Too low! ({remaining_guesses} guesses left)\n")
            elif guess > secret_number:
                print(f"Too high! ({remaining_guesses} guesses left)\n")
            else:
                print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
                return

        except ValueError:
            print("Please enter a valid number!\n")
            attempts -= 1

    print(f"\nGame over! The number was {secret_number}.")


guess_the_number()