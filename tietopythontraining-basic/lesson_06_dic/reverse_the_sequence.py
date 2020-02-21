# Given a sequence of integers that end with a 0. Print the sequence in reverse order.
#
# Don't use lists or other data structures. Use the force of recursion instead.


def sequence():
    number = int(input("provide"))
    if number != 0:
        sequence()
    print(number)


sequence()
