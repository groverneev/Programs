word = input("Enter a word.")
life = int(input("Enter the amount of lives you want."))
UsedLetters = ""
maskedWord = "*" * len(word)
inputLetter = ""
counter = len(word)
while life != 0 and word != maskedWord:
    inputLetter = input("Enter a letter.")
    for i in range(len(word)):
        if word(i) == letter_guessed:
            #do something to add it to the masked word
        counter = counter - 1
    if counter == 0:
        life = life - 1
        letter_guessed(guessCounter) = letter_guessed
    if counter == 1:
        print("hi")
