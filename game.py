"""A number-guessing game."""
import random
player = input("Welcome to the Guessing Game! Please enter your name: ")
number = random.randint(1, 100)
guess = int(input(f"Nice to meet you, {player}! I'm thinking of a number between 1 and 100. Guess the number: "))
guess_count = 1

while True:
  if guess > number:
      guess = int(input("The guess is too high. Try again: "))
      guess_count += 1
      print(guess_count)
  elif guess < number:
      guess = int(input("The guess is too low. Try again: "))
      guess_count += 1
      print(guess_count)
  else:
    print(f"Great job, {player}! You guessed the number in only {guess_count} tries.")
    exit()

