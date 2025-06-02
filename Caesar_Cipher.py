# Replicate one of the oldest known encryption by writing your own code.
# You can start with the following code:

# lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
# secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
# cipher = 7

# You can tackle this challenge using the skills you've learned so far in the course. 
# It might take you a moment to figure out a solution, but give it a try.

# Some concepts that you've learned about so far that might come in handy are looping, 
# conditional statements, string methods, slicing, and indexing.

# As a stretch task you could adapt your solution so that it preserves capitalization 
# of the original text, and that you can change the cipher to get a different encoding.

# Can you also write code to reverse the encryption?

lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7

def caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

encrypted = caesar(secret, cipher)
decrypted = caesar(encrypted, -cipher)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)

