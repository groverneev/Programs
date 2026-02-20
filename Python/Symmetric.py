myArray = [0] *20
myArray = input().split()
for counter in range(len(myArray)):
    myArray[counter] = int(myArray[counter])
x = len(myArray)
i = int(x/2)
y = 0
c = 0
for z in range(i):
    if myArray[z] != myArray[x-1]:
        print("Not Symmetric.")
        c = 1
        break
    x = x -1
    if (z > x):
        break
if(c==0):
    print("Symmetric.")
