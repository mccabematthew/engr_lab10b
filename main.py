# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: Matthew McCabe
# Section: 102 538
# Assignment: Lab 10b Act1
# Date: 10/31/2022
import random

print("Guess the secret integer between 1 and 100")
r = random.randint(1, 100)


def user_guess():
    g = int(input("What is your guess? "))
    return g


def is_less():
    if i < r:
        print("Too low, try again")
        user_guess()


def is_high():
    if i > r:
        print("Too high, try again")
        user_guess()

i = user_guess()
c = 1

while i != r:
    is_less()
    is_high()
    i = user_guess()
    c += 1

print(f'You found it in {c} guess(es)... PARTY TIME!!!')
