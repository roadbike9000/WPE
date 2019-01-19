"""
Write a program that asks the user, again and again, to enter a number.
(We will assume that the user will only enter integers.  The real world is a complex place, but we'll pretend that our
users are well behaved for the purposes of this exercise.)
When the user enters an empty string, then stop asking for additional inputs.

Along the way, as the user is entering numbers, I want you to store those numbers in a list.
I also want you to keep track of the minimum and maximum values that you've seen so far.

When the user has finished entering numbers, your program should print out:
The sum of these numbers
The average (mean) of these numbers
The largest and smallest numbers you received from the user
"""

# get input until the user enters empty string
list_of_numbers = []
value = input("Enter a number or press Enter to stop: ")
while value != "":
    list_of_numbers.append(int(value))
    smallest_number = min(list_of_numbers)
    largest_number = max(list_of_numbers)
    value = input("Enter a number or press Enter to stop: ")
total = sum(list_of_numbers)
mean = total / len(list_of_numbers)
print("Sum: {}".format(total))
print("Mean: {}".format(mean))
print("Largest number: {}".format(largest_number))
print("Smallest number: {}".format(smallest_number))
