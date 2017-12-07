 # This is a guess the number game.
import random

print("Hello. What is your name?")
name = input()

print("Hello, " + name + ". I'm thinking of a number between 1 and 20.")
secretNumber = random.randint(1,20)
print("DEBUG MODE: Secret number is: " + str(secretNumber))

 
for guessesTaken in range(1,7):
    print("Take a guess.")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low")
    elif guess > secretNumber:
        print("Your guess is too high")
    else:
        break
if guess == secretNumber:
    print("You figured it out in " + str(guessesTaken) + " guesses!")
else:
    print('Nope. The number was ' + str(secretNumber) + " .")