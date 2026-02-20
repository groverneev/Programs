keep_going = True
while (keep_going):
    print("Enter how many numbers you want in the Fibonacci Sequence:")
    a = input();
    b = int (a);
    first = 0
    second = 1
    for i in range(b):
        print(first)
        temporary = first
        first = second
        second = temporary+second
    answer = input ("Press enter to keep going or anything else to stop.")
    keep_going = (answer == "")
print("Thank you for playing!")
