import random
number = random.randint(1,100)
guess = 1000
while guess != number:
    guess = int(input("What is your guess?"))
    if guess < number:
        print("Greater")
    if guess > number:
        print("Less")
    if guess == number:
        print("Correct!")
        print("Thanks for playing with me!")
