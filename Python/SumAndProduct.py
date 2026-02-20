First = int(input("What is your first number?"))
Second = int(input("What is your second number?"))
Third = int(input("What is your third number?"))
if First + Second == Third:
    print("Your numbers are a sum of two.")
if First + Third == Second:
    print("Your numbers are a sum of two.")
if Second + Third == First:
    print("Your numbers are a sum of two.")
if First * Second == Third:
    print("Your numbers are a product of two.")
if First * Third == Second:
    print("Your numbers are a product of two.")
if Second * Third == First:
    print("Your numbers are a product of two.")
else:
    print("Your numbers are not a sum or product of two.")
