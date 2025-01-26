import random

print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number.")

print("Please select the difficulty level:")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)")

chances = 0
choice = input("Enter your choice: ")
if choice == "1":
  print("Great! You have selected the Easy difficulty level. \nLet's start the game!")
  chances = 10
elif choice == "2":
  print("Great! You have selected the Medium difficulty level. \nLet's start the game!")
  chances = 5
elif choice == "3":
  print("Great! You have selected the Hard difficulty level. \nLet's start the game!")
  chances = 3
else:
  print("You must enter an integer from 1 to 3!")
number = random.randint(1,100)
chances_left = chances
while chances_left > 0:
  guess = int(input("Enter your guess: "))
  chances_left -= 1
  if number > guess: 
    print(f"Incorrect! The number is greater than {guess}")
  elif number < guess:
    print(f"Incorrect! The number is less than {guess}")
  elif number == guess:
    print(f"Congratulations! You guessed the correct number in {chances - chances_left} attempts.")
    break
if chances_left == 0:
  print(f"The number is {number}")
