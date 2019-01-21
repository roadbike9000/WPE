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

text = {}
sentence = input("Please enter some text: ")
