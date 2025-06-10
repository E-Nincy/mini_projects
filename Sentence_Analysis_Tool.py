# Sentence Analysis Tool
# Write a script that takes a sentence from the user and returns:

# the number of lower case letters
# the number of uppercase letters
# the number of punctuations characters
# the total number of characters
# Use a dictionary to store the count of each of the above.

# Note: ignore all spaces.

# Example input:

# I love to work with dictionaries!
# Example output:

# Upper case: 1
# Lower case: 26
# Punctuation: 1
# Total chars: 28

import string

# Ask the user for a setence
sentence = input("Enter a sentence: ")

# Dictionary stpre result
char_count = {
    "upper": 0,
    "lower": 0,
    "punctuation": 0,
    "total": 0
}

# Loop through each character in the sentence
for char in sentence:
    if char == " ":
        continue
    elif char.isupper():
        char_count["upper"] += 1
    elif char.islower():
        char_count["lower"] += 1
    elif char in string.punctuation:
        char_count["punctuation"] += 1

    char_count["total"] += 1

#Print results
print(f"Upper case: {char_count['upper']}")
print(f"Lower case: {char_count['lower']}")
print(f"Punctuation: {char_count['punctuation']}")
print(f"Total chars: {char_count['total']}")