# Given a positive real number a and integer n.
# Compute a^n
#
# Write a function power(a, n) to calculate the results using the function and print the result of the expression.
#
# Don't use the same function from the standard library.


def power(a, n):
    result = 1
    if n > 0:
        for i in range(n):
            result *= a
        return result
    else:
        for i in range(abs(n)):
            result *= 1 / a
        return result


while True:
    try:
        a = int(input("a: "))
        n = int(input("n: "))
        print("negative exponent: " + str(power(a, n)))
        break
    except (SyntaxError, EOFError, ValueError, NameError, TypeError):
        print("wrong value try again !")
