# Given the year number. You need to check if this year is a leap year. If it is, print LEAP, otherwise print COMMON.
#
# The rules in Gregorian calendar are as follows:
#
#     a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
#     a year is always a leap year if its number is exactly divisible by 400
#
# Warning. The words LEAP and COMMON should be printed all caps.

while True:
    try:
        number = int(input("Provide a year number"))
        if number % 4 == 0 and number % 400 != 0 or number % 400 == 0:
            print("leap ")
        else:
            print("common")
    except (SyntaxError, EOFError, ValueError, NameError, TypeError):
        print("error")
