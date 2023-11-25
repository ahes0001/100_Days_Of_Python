from art import logo
import random

attempts = 5
notGuessed = True
randomNumber = random.randint(1,100)
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
diffculty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if diffculty.strip().lower() == "easy":
    attempts = 10

while attempts >0 and notGuessed:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = input("Make a guess: ")
    guess = int(guess.strip())
    attempts -= 1
    if guess>randomNumber:
        print("Too high")
    elif randomNumber>guess:
        print("Too low")
    elif randomNumber == guess:
        print("Well Done! You have guesssed correctly!")
        notGuessed = False
    else:
        print("ERROR!!!")

if notGuessed:
    print("GAME OVER!")
    print(f"The number was {randomNumber}")


