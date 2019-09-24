# Given N numbers: the first number in the input is N, after that N integers are given. Count the number of zeros
# among the given integers and print it.
#
# You need to count the number of numbers that are equal to zero, not the number of zero digits.

count = 0
while True:
    try:
        number = int(input("Provide number"))
        if number == 0:
            count += 1
        print("Zeros:" + str(count))
    except (SyntaxError, EOFError, ValueError, NameError, TypeError):
        print("it's not a int number")
