"""
ask the user to enter some text. Display the distribution of letters from within the text.
In other words, ask the user:
    Enter some text:

We'll then enter something:
    This is a test.  Show me the distribution, already!

Our program will:
Convert all letters to lowercase
Ignore characters that aren't lowercase letters
Create a dictionary in which the keys are letters and the values are the counts.
For each letter in the original string, show the number of times it was found, and the percentage of times of the total.
Example: Enter a string:     This is a test.  Show me the distribution, already!
    t: 6 15%
    h: 3 7%
"""
import string

count_letters = {}
sentence = input("Please enter some text: ").lower()
for letter in sentence:
    if letter in string.ascii_lowercase:
        if letter not in count_letters:
            count_letters[letter] = 1
        else:
            count_letters[letter] += 1
total_number_of_letters = sum(count_letters.values())
for letter, count in count_letters.items():
    print("{}: {} {}%".format(letter, count, int(count / total_number_of_letters * 100)))
