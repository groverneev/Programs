import sys
word = input("Enter a word.")
for i in range(len(word)):
    if word[i] != word[len(word) - i - 1]:
        print("Your word is not a palindrome.")
        sys.exit()
print("Your word is a palindrome!")