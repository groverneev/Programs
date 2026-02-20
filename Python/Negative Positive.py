keep_going = True
while (keep_going):
    print("Enter a number.")
    a = input();
    b = int (a);
    if (b == 0):
        print ("You entered the number 0.")
    if (b < 0):
        print ("You chose a negative number.")
    if (b > 0):
        print ("You chose a positive number.") 
    answer = input ("Press enter to keep going or anything else to stop.")
    keep_going = (answer == "")
print("Thank you for playing!")
