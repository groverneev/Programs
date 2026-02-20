n, q = map(int, input().split())
time = []
timeaftertask = []
totaltime = 0
for _ in range(n):
    e = int(input())
    time.append(e)
    totaltime += e
    timeaftertask.append(totaltime)
for __ in range(q):
    question = int(input())
    if question == 0:
        print(1)
    else:
        for i in range(len(timeaftertask)):
            if question < timeaftertask[i]:
                print(i+1)
                break