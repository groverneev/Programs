import sys
keep_going = True
while (keep_going):
    print("Enter a number.")
    string = input ();
    x = int(string)
    for z in range (1, x+1):
        y = x % z
        if (y == 0):
            print (z, "is a factor of", x,".")
    answer = input ("Press enter to keep going or anything else to stop.")
    keep_going = (answer == "")
print("Thank you for playing!")
