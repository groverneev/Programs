import time
import random
wrong = False
counter = 1
answer = ""
guess = ""
IQ = -1
print("Neev has a high score of 12 digits, or 300 IQ.")
print("Can you beat this high score?")
print("\n\n")
while wrong != True:
    print("Your number is:", end = " ")
    for a in range(counter):
        e = random.randint(1, 9)
        print(e, end = "")
        e = str(e)
        answer = answer + e
        e = int(e)
    print("")
    print("You now have", counter, "second to memorize this number.")
    time.sleep(counter)
    for b in range(50):
        print("")
    d = int(input("You now have to write the number that you just saw."))
    guess = d
    print("Your guess is:", guess)
    print("The correct answer is:", answer)
    guess = int(guess)
    answer = int(answer)
    if guess != answer:
        wrong = True
        print("Your answer is wrong.")
    if guess == answer:
        print("Your answer is correct!")
        print("\n\n")
    counter = counter + 1
    answer = ""
    guess = ""
    IQ = IQ + 1
if IQ == 1:
    print("You got", IQ, "question correct.")
if IQ != 1:
    print("You got", IQ, "questions correct.")
print("Your final IQ is:", IQ*25)
if (IQ*25) > 300:
    print("You now have the highest score in the game!")