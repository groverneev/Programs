print ("Enter the number you want a multiplication table for or '0' to quit:")
string = input();
i = int (string);
while (i !=  0):
    z = i % 2
    if z == 0:
        print("You have picked an even number.")
    else:
        print("You have picked an odd number.")
    for x in range (1,11):
        y = i* x
        print(i, " * ", x, "=", y)
    string = input ("Enter the number you want a multiplication table for or '0' to quit:\n")
    i = int (string)
