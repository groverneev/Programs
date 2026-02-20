myarray = [] * 10
myarray = input().split()
x = len(myarray)
counter = 0
for counter in range(x):
    myarray[counter] = int(myarray[counter])
counter = 0
tally = [0] * 1001

for i in range (x):
    tally[myarray[i]] = tally[myarray[i]] + 1

for j in range (1000):
    if tally[j] > 1:
        print (j)
