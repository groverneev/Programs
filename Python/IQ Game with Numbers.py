import time
import random
wrong = False
counter = 1
answer = []
guess = []
IQ = -1
print("Neev has a high score of 3 questions, or 150 IQ.")
print("Can you beat this high score?")
print("\n\n")
while wrong != True:
    if counter == 1:
        print("Your number is:", end = " ")
    if counter != 1:
        print("Your numbers are:", end = " ")
    for a in range(counter - 1):
        e = random.randint(10, 99)
        print(e, end = ", ")
        answer.append(e)
    e = random.randint(10, 99)
    print(e)
    answer.append(e)
    print("You now have", counter*2, "seconds to memorize these numbers.")
    time.sleep(counter*2)
    for b in range(40):
        print("")
    if counter == 1:
        print("You now have to write the number that you just saw.")
    if counter != 1:
        print("You now have to write the numbers that you just saw.")
    for c in range(counter):
        d = int(input())
        guess.append(d)
    print("Your guess is:", guess)
    print("The correct answer is:", answer)
    if guess != answer:
        wrong = True
        print("Your answer is wrong.")
    if guess == answer:
        print("Your answer is correct!")
        print("\n\n")
    counter = counter + 1
    answer = []
    guess = []
    IQ = IQ + 1
if IQ == 1:
    print("You got", IQ, "question correct.")
if IQ != 1:
    print("You got", IQ, "questions correct.")
print("Your final IQ is:", IQ*50)
if (IQ*50) > 300:
    print("You now have the highest score in the game!")
