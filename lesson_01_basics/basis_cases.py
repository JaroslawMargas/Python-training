import re
import math

# Write a program that greets the person by printing the word "Hi" and the name of the person. See the examples below.
reg = r'[a-zA-Z]'
expected = re.compile(reg)
while True:
    input_name = input("Your Name?")
    # Python 3+ input instead
    if expected.search(input_name):
        print('Hi ' + input_name)
        break


# Write a program that takes three numbers and prints their sum. Every number is given on a separate line.

def error_value_print():
    print('that is not a proper value')


def get_value(str_value):
    while True:
        try:
            number = float(input('Provide ' + str(str_value)))
            return number
        except (SyntaxError, EOFError, ValueError, NameError, TypeError):
            error_value_print()


num_one = get_value('number one')
num_two = get_value('number two')
num_three = get_value('number three')

sum_num = num_one + num_two + num_three
sum_numbers = round(sum_num, 6)

print('Sum is ' + str(sum_numbers))

# N students take K apples and distribute them among each other evenly. The remaining (the undivisible)
# part remains in the basket. How many apples will each single student get? How many apples will remain in the basket?
# The program reads the numbers N and K. It should print the two answers for the questions above.

students = get_value('of students')
apples = get_value('of apples')
if students > 0:
    print(str(apples // students) + " gets each student")
    # the floor division // rounds the result down to the nearest whole number
    print("remains " + str(apples % students))
else:
    print("wrong values to divide")
    print("remains " + str(apples))

# A school decided to replace the desks in three classrooms. Each desk sits two students.
# Given the number of students in each class, print the smallest possible number of desks that can be purchased.
# The program should read three integers: the number of students in each of the three classes, a, b and c respectively.

# number of students
x = students // 2 + students % 2
# example 123 // 2 = (122/2=61) + (123%2 = 122/2 and rest 1) =  61 + 1

print("For " + str(students) + " needs desk " + str(x))

# Given an integer number, print its last digit.
num = 1234
print("Last digit " + str(num) + " is: " + str(int(num) % 10))
# example 987 /10 = 980/10 rest 7

# Given an integer. Print its tens digit.
num = 1234
print("The tens digit " + str(num) + " is: " + str((int(num) % 100) // 10))
# example 1234 % 100 = 1200/100 rest 34
# 34 // 10  = 30 / 10 = 3

# Given a positive real number, print its fractional part.
num = 123.456
print("Fractional " + str(num) + " is: " + str(round((num % 1), 6)))

# Given a positive real number, print its first digit to the right of the decimal point.
# real numbers are represented as floats
num = 123.456
fractional = num % 1
dig_right = int(fractional * 10)
print("First digit to the r side of decimal " + str(num) + " is: " + str(dig_right))

# Car route
km_per_day = input("How many km per day ?")
km = input("How many km would you like to ride?")
# round float up to int
print("You need a " + str(math.ceil(int(km) / int(km_per_day))) + " days for this distance")

# Given the integer N - the number of minutes that is passed since midnight -
# how many hours and minutes are displayed on the 24h digital clock?
# The program should print two numbers: the number of hours (between 0 and 23)
# and the number of minutes (between 0 and 59).
# For example, if N = 150, then 150 minutes have passed since midnight - i.e. now is 2:30 am.
# So the program should print 2 30

N = input("Number of minutes ?")
hour = int(N) // 60
min_val = int(N) % 60
print(str(hour) + ":" + str(min_val))

# Total cost
# A cupcake costs A dollars and B cents. Determine, how many dollars and cents should one pay for N cupcakes.
# A program gets three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.

# 1,10 = 1 + 0,10
# 12 pcs
# 12 + 1,20 =  13,20

while True:
    try:
        A = int(input("How many dol one ?"))
        B = int(input("How many cents one ?"))
        N = int(input("How many cupcake ?"))
        break
    except (ValueError, TypeError):
        print('try again')

dol_tmp = N * A
# 12 * 1 dol = 12
cent_tmp = N * B
# 12* 10 = 120
dol = dol_tmp + cent_tmp // 100
# 12 + 120//100 = 12+1 =13
cent = cent_tmp % 100
# 120 % 100  = 20

print("you will pay dol: " + str(dol) + " and cent: " + str(cent))
