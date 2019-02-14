"""
This week, I want you to write a new, related function called `check_isbns`.  Notice that the function name implies that
we're going to accept a number of ISBNs passed to us. But this function will actually take two arguments:
the first argument is a string, naming the file into which the function should print its report
all further arguments are ISBNs that should be checked

In other words, we can call this function with a number of arguments, each of which will be checked to see if it's a
valid ISBN.  The function will put its assessment of each ISBN in a file.  Each line in the file will contain two
values, the ISBN being checked and one of three values:
True (indicating it's valid)
False (indicating it's not valid)
bad length of x (where "x" is the length, and it's not 13)

In other words, I can say:
    check_isbns('mybooks.txt', '12345', '9780525533184', '9780143127793')

and if I do so, then the file will contain three lines:
    12345    bad length of 5
    9780525533184    True
    9780143127799    False
"""

def validate_isbns(filename, *args):
    with open(filename, 'w') as outfile:
        for user_isbn in args:
            isbn = ''
            for digit in user_isbn:
                if digit.isdigit():
                    isbn += digit
                    check_digit = isbn[-1]  # last digit of isbn is check sum

            is_valid = False  # flag indicating whether isbn is valid or not. Default is False

            # if isbn is not 13 digits long log it as bad length
            if len(isbn) != 13:
                outfile.write(f'{isbn}\tbad length of {len(isbn)}\n')
                continue

            # process valid isbn, calculate sum, get final digit to compare with check sum
            # multiply the value of each odd index by 1
            # multiply the value of each even index by 3
            isbn_total = 0  # store sum of isbn

            for index, number in enumerate(isbn[:12]):
                if index % 2:  # if index is odd 3 * number
                    isbn_total += int(number) * 3
                else:
                    isbn_total += int(number)

            user_check_digit = 10 - (isbn_total % 10)
            if user_check_digit == 10:
                user_check_digit = 0

            # refactor to return "True" or "False"
            if user_check_digit == int(check_digit):
                is_valid = True

            outfile.write(f'{isbn}\t{is_valid}\n')
