"""
Pytest tests for A1 Exercise 3 solution
"""

import pytest


def check_isbns(filename, *isbns):
    isbn_data_file = open(filename, 'w')
    isbn_data_file.close()


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

    check_isbns(filename, test_isbns)

    for one_line in open(filename):
        print(one_line)
        isbn, assessment = one_line.rstrip().split('\t')

        assert assessment == test_isbns[isbn]
