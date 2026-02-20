keep_going = True
while (keep_going):
    factorial = 1
    a = int(input("Enter a number that is greater than 1 and a whole number."))
    if (a < 1):
            print("Sorry, your number needs to be greater than than 1.")
    for i in range(1, a + 1):
        factorial = factorial*i
    print ("The factorial of" ,a, "is" ,factorial, ".")
    answer = input ("Press enter to keep going or anything else to stop.")
    keep_going = (answer == "")
print("Thank you for playing!")
