import sys
keep_going = True
while (keep_going):
    print("Enter a number.")
    string = input ();
    x = int(string)
    notprime = 0
    for z in range (2, x-1):
        y = x % z
        if (y == 0):
            notprime = 1
    if (notprime != 1):
        print (x, "is a prime number.")
    else:
        print (x, "is a composite number.")
    answer = input ("Press enter to keep going or anything else to stop.")
    keep_going = (answer == "")
print("Thank you for playing!")
