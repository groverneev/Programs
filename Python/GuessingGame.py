import random
x = int(input("What is your first number?"))
y = int(input("What is your last number?"))
number = random.randint(x, y)
print("Guess a number between",x,"and",y,":")
guess = int(input())
counter = 0
while guess != number:
    if guess > number:
        print(guess, "was too high. Try again.")
    if guess < number:
        print(guess, "was too low. Try again.")
    guess = int(input("Guess again: "))
    counter = counter + 1
print("You have used",counter + 1, "guesses.")
print(guess, "was the number! You win!")
