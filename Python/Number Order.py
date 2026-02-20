def compare_three_int (d, e, f):
    if (d <= e):
        if (f > e):
            print ("Numbers in ascending order:",d,",",e,",",f)
        elif (f > d):
            print ("Numbers in ascending order:",d,",",f,",",e)
        else:
            print ("Numbers in ascending order:",f,",",d,",",e)
    else: # e < d
        if (f > d):
            print ("Numbers in ascending order:",e,",",d,",",f)
        elif (f > e):
            print ("Numbers in ascending order:",e,",",f,",",d)
        else:
            print ("Numbers in ascending order:",f,",",e,",",d)
keep_going = True
while (keep_going):
    a = input("Enter a number that is not a decimal or a fraction.")
    b = input("Enter another number that is not a decimal or a fraction.")
    c = input("Enter one last number that is not a decimal or a fraction.")
    d = int (a);
    e = int (b);
    f = int (c);
    compare_three_int (d, e, f)
    answer = input ("Press enter to keep going or anything else to stop.")
    keep_going = (answer == "")
print("Thank you for playing!")
