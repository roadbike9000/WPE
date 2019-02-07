"""
First: Last time, we asked the user for input, and then fed that input to our ISBN-checking algorithm.
This time, the idea is to write a function called "validate_isbn", which will return a "True" or "False" value.
(Note: The function won't print anything.  It'll return a value, which can then be printed by whoever calls the
function.)  The input to the function should be a string, and that string can contain any number of characters.
We'll ignore the non-numeric characters; if 13 numeric characters remain, then we'll return "True" or "False" to
indicate whether the ISBN is valid.
Second: If we receive too few or too many digits, then we'll raise a TypeError exception.
"""

def validate_isbn(isbn):
    is_valid = False    # flag indicating whether isbn is valid or not. Default is False
    # remove the dash
    isbn_numbers = [int(digit) for digit in isbn if digit.isdigit()]
    # get the last digit as check sum
    check_sum = isbn_numbers[-1]
    isbn_sum = 0
    # multiply the value of each odd index by 1
    # multiply the value of each even index by 3
    for index, number in enumerate(isbn_numbers[:-12]):
        isbn_sum += (number * 3 if index % 2 else number)

    if isbn_sum % 10 == 0:
        final_digit = 0
    else:
        final_digit = 10 - (isbn_sum % 10)

    # refactor to return "True" or "False"
    if final_digit == check_sum:
        is_valid = True

    return is_valid

import pytest

@pytest.mark.parametrize('isbn', [
    '',
    '12345',
    '123456789012345',
    ])
def test_bad_isbn_length(isbn):
    with pytest.raises(TypeError) as e:
        validate_isbn(isbn)
    assert e.value.args[0].endswith(f', not {len(isbn)}')

@pytest.mark.parametrize('isbn', [
    '9780143127796',
    '9780415700108',
    '9780525533184',
    ])
def test_good_isbn(isbn):
    assert validate_isbn(isbn)

@pytest.mark.parametrize('isbn', [
    '9780143127793',
    '9780415700103',
    '9780525533183',
    ])
def test_bad_isbn(isbn):
    assert validate_isbn(isbn) == False