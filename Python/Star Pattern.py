counter = 4
nextcounter = 1
for a in range(5):
    for z in range(counter):
        print(" ", end = "")
    for z in range(nextcounter):
        print("•", end = "")
    for z in range(counter):
        print(" ", end = "")
    print("")
    counter -= 1
    nextcounter += 2