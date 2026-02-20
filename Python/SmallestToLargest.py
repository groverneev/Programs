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
    if Second < Third:
        print(Small,",",Second,",",Third)
    else:
        print(Small,",",Third,",",Second)
if Small == Second:
    if First < Third:
        print(Small,",",First,",",Third)
    else:
        print(Small,",",Third,",",First)
if Small == Third:
    if First < Second:
        print(Small,",",First,",",Second)
    else:
        print(Small,",",Second,",",First)
