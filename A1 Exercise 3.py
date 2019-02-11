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

