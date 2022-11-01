import random
# print("Welcome to the number Guessing Game!\nI'm thinking of a number between 1 and 100.")
# comp=random.randint(1,100)
# diff=input("Choose a difficulty. Type 'easy' or 'hard' : ")
# if diff=="easy":
#   n=10
#   print("You have 10 attempts remaining to guess the number.")
# elif diff=="hard":
#   n=5
#   print("You have 5 attempts remaining to guess the number.")
# cond=True
# while cond==True:
#  if n==0:
#    print("You've run out of guesses, you lose.")
#    cond=False
#  else:
#   guess=int(input("Make a guess: "))
#   if diff=="easy":
#     if guess>comp:
#       print("Too high.\nGuess again.")
#       n-=1
#       print(f"You have {n} attempts remaining to guess the number.")
#       cond=True
#     elif guess<comp:
#       print("Too low.\nGuess again.")
#       n-=1
#       print(f"You have {n} attempts remaining to guess the number.")
#       cond=True
#     elif guess==comp:
#       print(f"You got it! The answer was {comp}.")
#       cond=False
#   elif diff=="hard":
#     if guess>comp:
#       print("Too high.\nGuess again.")
#       n-=1
#       print(f"You have {n} attempts remaining to guess the number.")
#       cond=True
#     elif guess<comp:
#       print("Too low.\nGuess again.")
#       n-=1
#       print(f"You have {n} attempts remaining to guess the number.")
#       cond=True
#     elif guess==comp:
#       print(f"You got it! The answer was {comp}.")
#       cond=False
# print("Thank's For Playing.")   
