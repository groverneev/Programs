# https://usaco.org/index.php?page=viewproblem2&cpid=891

read = open("shell.in")
score = [0, 0, 0]
arr = [1, 2, 3]
for i in range(int(read.readline())):
    a, b, g = [int(i) - 1 for i in read.readline().split()]
    # Swap the elements
    arr[a], arr[b] = arr[b], arr[a]
    test = arr[g]
    if (test == 1):
        score[0] += 1
    elif (test == 2):
        score[1] += 1
    elif (test == 3):
        score[2] += 1
print(max(score), file=open("shell.out", "w"))
