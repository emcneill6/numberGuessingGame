# Emma McNeill
# Purpose: the purpose of this program is to play a numbers guessing game

# have the program generate a random number between 1 and 100
import random

number = random.randint(1, 100)


while True:

    try:

        print("Welcome to the Number Guessing Game!")
        print()
        # give the user a way to quit the game
        print("If you would like to exit the game at anytime, press enter.")
        print()
        # have user enter a guess
        guess = int(input("Guess an integer between 1 and 100:  "))
        print()

        # keep track of how many guesses
        count = 1

        while number != guess:
            count = count + 1

            if guess > number:
                print(f"Your guess is too high. Please try again.")
                print()
                guess = int(input("Enter an integer between 1 and 100:  "))
                print()

            if guess < number:
                print(f"Your guess is too low. Please try again.")
                print()
                guess = int(input("Enter an integer between 1 and 100:  "))
                print()

        if guess == number:
            print(f'Good job! You won in {count} guesses!')


    except ValueError as e:
     print(f"Ending game...")
     print(f"\t{e}")

    finally:
      print(f" Thanks for playing! ".center(20, "="))
      print()