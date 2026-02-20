f, k = map(int, input().split())
arr = [0]*f
for i in range(k): 
    start, interval = map(int, input().split())
    for j in range(start, len(arr)+1, interval): 
        arr[j-1] += 1
counter = 0
for _ in range(len(arr)): 
    if arr[_] == 0:
        counter += 1
print(counter)