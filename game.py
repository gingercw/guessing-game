"""A number-guessing game."""
import random
number = random.randint(1, 100)
player = input("Welcome to the Guessing Game! Please enter your name: ")
guess = input(f"Nice to meet you, {player}! I'm thinking of a number between 1 and 100. Guess the number: ")

