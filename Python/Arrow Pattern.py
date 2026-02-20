import sys
while True:
    a = input("Do you want up (u), left (l), right (r), or q to quit?")
    if a == "q":
        print("Thank you for playing!")
        sys.exit()
    elif a == "u":
        counter1 = 4
        counter2 = 0
        for b in range(5):
            for z in range(counter1):
                print(" ", end = "")
            print("•", end = "")
            for z in range(counter2):
                print(" ", end = "")
            if counter2 != 0:
                print("•")
            for z in range(counter1):
                print(" ", end = "")
            print()
            counter1 -= 1
            counter2 += 2
            if a == 1:
                counter2 -= 1
    else:
        print("Sorry, your input is invalid. Please enter a valid input.")