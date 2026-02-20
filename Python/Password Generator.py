import random
import string
characters = list(string.ascii_letters + string.digits + "!@#$%^&")
random.shuffle(characters)
a = int(input("How many passwords do you want?"))
for b in range(a):
    print("Enter a password length for password #", end = "")
    print(b + 1)
    length = int(input())
    random.shuffle(characters)
    password = []
    for i in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)
    print("".join(password))