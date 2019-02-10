"""
This week, we'll start off by calculating checksums.  And we'll do it with an algorithm near and dear to my heart,
calculating the checksum for ISBN-13.

Along the way, we'll practice:
    Getting input from the user
    Converting data from strings to integers (and back)
    Iterating with "for" loops
    Using the "enumerate" method
    Some basic math operations, including % (modulus)

You see, every book published in the world has (or should have) a unique ISBN (international standard book number).
This allows everyone from publishers to bookstores to keep track of all of the books out there, even if different books
have the same name. If you have experience with databases, you can think of ISBNs as the primary key of the book world.

For example: On my desk, I have a book called "Artificial Unintelligence," by Meredith Broussard, which I recently
started to read, and which is quite fascinating.  But we'll ignore the content right now, and concentrate on its
ISBN-13, which is 978-0262038003.

The thing is, an ISBN-13 isn't just a serial number. The final digit is a "checksum," meaning that it helps to ensure
that the previous digits weren't entered incorrectly.  If someone were to enter 978-0262038002 (notice that there's a
2 at the end, rather than a 3), then we would know that the ISBN-13 was impossible, and thus incorrect.

How is the checksum digit calculated? Through a pretty simple algorithm: We take the first 12 digits, and multiply each
one by either 1 or 3, alternating between them.  We then take the sum and divide it by 10, taking the remainder.
That remainder will be a digit between 0 and 9.  We subtract the remainder from 10, and *that's* the final digit.

In other words, if we take my book's ISBN-13:
    978-0262038003

Let's go through the first 12 digits:
    978026203800

We now multiply each digit by either 1 or 3, starting with 1, and alternating between them:
    9 + 3*7 + 8 + 3*0 + 2 + 3*6 + 2 + 3*0 + 3 + 3*8 + 0 + 3*0

The total is 87.  We can then divide this by 10, getting a remainder of 7.  10 - 7 = 3, and sure enough, 3 should be the
final digit.

For this week, your exercise is to ask the user to enter an ISBN, and to indicate whether it is valid or not.
For example:
    Enter an ISBN: 9780262038003
    Yes, valid
    Enter an ISBN: 9780262038002
    No, invalid
"""


def check_if_valid_isbn(user_isbn):
    is_valid = False    # initialize flag to false
    # remove the dash
    isbn = [int(digit) for digit in user_isbn if digit.isdigit()]
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

    if final_digit == check_sum:
        is_valid = True

    if is_valid:
        print(f"{user_isbn} is a valid ISBN")
    else:
        print(f"{user_isbn} is not a valid ISBN")


isbn = ""
while len(isbn) != 14:
    isbn = input("Enter an ISBN: ").strip()

check_if_valid_isbn(isbn)



