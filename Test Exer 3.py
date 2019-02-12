"""
Pytest tests for A1 Exercise 3 solution
"""

import pytest


def validate_isbns(filename, *args):
    with open(filename, 'w') as outfile:
        for user_isbn in args:

            # check each isbn for non-digit and rebuild the isbn
            isbn = [int(digit) for digit in user_isbn if digit.isdigit()]

            is_valid = False  # flag indicating whether isbn is valid or not. Default is False

            # if isbn is not 13 digits long log it as bad length
            if len(isbn) != 13:
                outfile.write(f'{isbn}\tbad length of {len(isbn)}\n')
                continue

            # process valid isbn, calculate sum, get final digit to compare with check sum
            # multiply the value of each odd index by 1
            # multiply the value of each even index by 3
            isbn_sum = 0  # store sum of isbn
            check_sum = isbn[-1]  # last digit of isbn is check sum

            for index, number in enumerate(isbn[:12]):
                isbn_sum += (number * 3 if index % 2 else number)

            if isbn_sum % 10 == 0:
                final_digit = 0
            else:
                final_digit = 10 - (isbn_sum % 10)

            # refactor to return "True" or "False"
            if final_digit == check_sum:
                is_valid = True

            outfile.write(f'{isbn}\t{is_valid}\n')


def test_isbn_checker(tmp_path):
    test_directory = tmp_path / 'testfiles'
    test_directory.mkdir()
    filename = test_directory / 'outfile.txt'

    test_isbns = {'': 'bad length of 0',  # empty; invalid
                  '12345': 'bad length of 5',
                  '123456789012345': 'bad length of 15',
                  '9780143127796': 'True',
                  '9780415700108': 'True',
                  '9780525533184': 'True',
                  '9780143127793': 'False',
                  '9780415700103': 'False',
                  '9780525533183': 'False'}

    validate_isbns(filename, *test_isbns)

    for one_line in open(filename):
        print(one_line)
        isbn, assessment = one_line.rstrip().split('\t')

        assert assessment == test_isbns[isbn]
