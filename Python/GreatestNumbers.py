First = int(input("What is your first number?"))
Second = int(input("What is your second number?"))
Third = int(input("What is your third number?"))
if First < Second:
    if Third < First:
        Small = Third
    else:
            Small = First
else:
    if Second < Third:
        Small = Second
    else:
        Small = Third
if Small == First:
    print("The greatest numbers are",Second,"and",Third,".")
if Small == Second:
    print("The greatest numbers are",First,"and",Third,".")
if Small == Third:
    print("The greatest numbers are",First,"and",Second,".")
