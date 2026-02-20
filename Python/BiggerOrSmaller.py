keep_going = True
while (keep_going):
    a = input("Enter a number that is not a decimal or a fraction.")
    b = input("Enter another number that is not a decimal or a fraction.")
    c = int (a);
    d = int (b);
    if (c < d):
        print(c, "is smaller than", d,".")
    if (c > d):
        print(c, "is greater than", d,".")
    if (c == d):
        print(c, "is equal to", d,".")
    answer = input ("Press enter to keep going or anything else to stop.")
    keep_going = (answer == "")
print("Thank you for playing!")
