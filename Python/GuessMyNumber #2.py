import random
print("Come up with a secret integer in your head from 1 - 100")
print("")
print("Now I will try to guess your number.")
print("")
print("Print '1' if the number is greater, print '-1 if the number is less, and print 0 if the number is correct.")
less = 1
greater = 100
output = 1000
rr = random.randint(less + 1,greater - 1)
print(rr)
while output != 0:
    output = int(input())
    if output == 1:
        less = rr
        rr = random.randint(less + 1,greater - 1)
        print(rr)
    if output == -1:
        greater = rr
        rr = random.randint(less + 1,greater - 1)
        print(rr)
    if output == 0:
        print("Thanks for playing with me!")
