myarray = []
myarray = input().split()
y = 0
false_a = []
zero_a = []
x = len(myarray)
for y in range(x):
    if int(myarray[y]) == 0:
        zero_a.append(myarray[y])
    else:
        false_a.append(myarray[y])
print(zero_a,false_a)
