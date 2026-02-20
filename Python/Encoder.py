"""
message = input("Enter a message to encode.")
key = eval(input("Enter a key value from 1 - 25."))
message = message.upper()
output = ""
for letter in message:
    if letter.isupper():
        value = ord(letter) + key
        letter = chr(value)
        if not letter.isupper():
            value -= 26
            letter = chr(value)
    output += letter
output = output.lower()
print("Here is your encoded message:", output)
print("Here is the key to decode this message:", key)
"""

import base64
print("Encoded Message: " + base64.b64encode(input("Enter a message to encode: ").encode('utf-8')).decode('utf-8'))