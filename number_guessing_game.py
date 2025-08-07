import random

while True:

    secret_number = random.randint(1,100)
    guess_number = None
    guess_count = 0
    print("Welcome to the Number Guessing Game!")

    while guess_number != secret_number:
        guess_number = int(input("Please Guess any nymber between 1 and 100: "))
        guess_count += 1

        if guess_number < secret_number:
            print("The number is too low")
        elif guess_number > secret_number:
            print("The number is too high")
        
    print(f"Correct! You guessed the number {guess_number} out of {guess_count} tries")

    play_again = input("Do you want to play again?(Yes/No): ").lower()

    if play_again.lower() != "yes":
        print("Thanks for palying!")
        break
