"""
First: Last time, we asked the user for input, and then fed that input to our ISBN-checking algorithm.
This time, the idea is to write a function called "validate_isbn", which will return a "True" or "False" value.
(Note: The function won't print anything.  It'll return a value, which can then be printed by whoever calls the
function.)  The input to the function should be a string, and that string can contain any number of characters.
We'll ignore the non-numeric characters; if 13 numeric characters remain, then we'll return "True" or "False" to
indicate whether the ISBN is valid.
Second: If we receive too few or too many digits, then we'll raise a TypeError exception.
"""


def validate_isbn(user_isbn):
    is_valid = False    # flag indicating whether isbn is valid or not. Default is False

    # remove the dash
    isbn = [int(digit) for digit in user_isbn if digit.isdigit()]
    if len(isbn) != 13:
        raise TypeError(f'A valid ISBN is 13 digits, not {len(isbn)}')

    # get the last digit as check sum
    check_sum = isbn[-1]
    isbn_sum = 0

    # multiply the value of each odd index by 1
    # multiply the value of each even index by 3
    for index, number in enumerate(isbn[:12]):
        isbn_sum += (number * 3 if index % 2 else number)

    if isbn_sum % 10 == 0:
        final_digit = 0
    else:
        final_digit = 10 - (isbn_sum % 10)

    # refactor to return "True" or "False"
    if final_digit == check_sum:
        is_valid = True

    return is_valid
