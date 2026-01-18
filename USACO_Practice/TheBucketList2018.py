# https://usaco.org/index.php?page=viewproblem2&cpid=856

arr = []
with open("blist.in") as read:
    for _ in range(int(read.readline())):
        arr.append(list(map(int, read.readline().split())))

largest = int(max(subarray[1] for subarray in arr))

maxbuckets = 0
currbuckets = 0
for i in range(1, largest + 1):
    arr2 = list(subarray[0] for subarray in arr) #new cow
    if (i in arr2):
        for j in range(len(arr)):
            if (arr[j][0] == i):
                currbuckets += arr[j][2]
                if (currbuckets > maxbuckets):
                    maxbuckets = currbuckets
    else:
        arr2 = list(subarray[1] for subarray in arr) # leaving cow
        if (i in arr2):
            for j in range(len(arr)):
                if (arr[j][1] == i):
                    currbuckets -= arr[j][2]
        else:
            pass
with open("blist.out", "w") as out:
    print(maxbuckets, file=out)
