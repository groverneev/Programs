First = int(input("What is your first number?"))
Second = int(input("What is your second number?"))
Third = int(input("What is your third number?"))
if First < Second:
    if Third < First:
        print("The smallest number is",Third,".")
    else:
            print("The smallest number is",First,".")
else:
    if Second < Third:
        print("The smallest number is",Second,".")
    else:
        print("The smallest number is",Third,".")
