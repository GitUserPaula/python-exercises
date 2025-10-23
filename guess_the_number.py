import random
import os

print ("Welcome to Guess the Number!")

secret_number = random.randint(1, 10)
guess_attempts = 0
max_attempts = 5

#player_guess = int(input("Please enter your guess (between 1 and 10): "))

while guess_attempts < max_attempts:

    try:
        player_guess = int(input("Please enter your guess (between 1 and 10): "))
        guess_attempts += 1
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 10")
        continue

    if player_guess == secret_number:
        print("Congrats! you have guessed the number")
        break
    elif player_guess < secret_number:
        print("Too low! try again")
    else:
        print("too high! try again")
    
else:
    print(f"Sorry you have used all your attempts. The secret number was {secret_number}")


"""os.system('cls')
print("Game over. Thanks for playing!")"""

