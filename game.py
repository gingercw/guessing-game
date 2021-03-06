"""A number-guessing game."""
import random
player = input("Welcome to the Guessing Game! Please enter your name: ")
number = random.randint(1, 100)
guess = input(f"Nice to meet you, {player}! I'm thinking of a number between 1 and 100. Guess the number: ")
guess_count = 1

while True:
  try:
    guess = int(guess)
    if guess < 1 or guess > 100:
        guess = input("Whomp whomp. That guess is not between 1-100. Try again: ")
        guess_count += 1
    elif guess != number and guess >= 1 and guess <= 100:
        guess = input("The guess is too high. Try again: ") if guess > number else input("The guess is too low. Try again: ")
        guess_count += 1
    else:
      print(f"Great job, {player}! You guessed the number in only {guess_count} tries.")
      exit()
      break
  except ValueError:
    guess = input("That's not a number... Try again: ")
    guess_count += 1



