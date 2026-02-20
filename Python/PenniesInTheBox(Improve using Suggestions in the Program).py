import random
pennies = []
counter = 0
score1 = 0
score2 = 0
boxes = int(input("Enter the number of boxes:"))
pennies = input("Enter the number of pennies in each box:").split()
random.shuffle(pennies)
player1 = input("Enter player 1's name.")
player2 = input("Enter player 2's name.")
x = len(pennies)
for counter in range(x):
    pennies[counter] = int(pennies[counter])
while x !=0:
    print("Boxes:")
    print(pennies)
    print(player1,"'s score:",score1)
    print(player2,"'s score:",score2)
    print("Enter",player1,"'s move (1 for leftmost, 2 for rightmost.")
    move = int(input())
    if move == 1:
        score1 = score1 + pennies[0]
        pennies.pop(0)
    if move == 2:
        score1 = score1 + pennies[x-1]
        pennies.pop(x-1)
    x = len(pennies)
    if x == 0:
        break
    print("Boxes:")
    print(pennies)
    print(player1,"'s score:",score1)
    print(player2,"'s score:",score2)
    print("Enter",player2,"'s move (1 for leftmost, 2 for rightmost.")
    move = int(input())
    if move == 1:
        score2 = score2 + pennies[0]
        pennies.pop(0)
    if move == 2:
        score2 = score2 + pennies[x-1]
        pennies.pop(x-1)
    x = len(pennies)
print(player1,"'s score:",score1)
print("Player 2's score:",score2)
if score1 > score2:
    print(player1,"wins!")
if score1 < score2:
    print(player2,"wins!")
if score1 == score2:
    print("It's a rare tie!")

#Things to improve:
    #1. Check for invalid commands(for example, a, 4, !, etc)
    #2. The array must be at least 5 spaces or longer
    #3. Have a coin toss in the beginning (random function) to choose who goes first
    #4. Enter 3 for undo (only one opportunity)
    #5. Make an app on the game.
    #6. Construct a Pennies in the Box engine
    #7. Make the code shorter and easier to read
