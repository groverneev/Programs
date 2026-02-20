"""
message = input("Enter a message to decode.")
key = eval(input("Enter a key value from 1 - 25."))
message = message.upper()
output = ""
for letter in message:
    if letter.isupper():
        value = ord(letter) - key
        letter = chr(value)
        if not letter.isupper():
            value += 26
            letter = chr(value)
    output += letter
output = output.lower()
print("Here is your decoded message:", output)
"""

import base64
print("Decoded Message: " + base64.b64decode(input("Enter the message to decode: ").encode('utf-8')).decode('utf-8'))