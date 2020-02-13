# In mathematics, the factorial of an integer n, denoted by n! is the following product:
# n!=1×2×…×n
#
# For the given integer n
# calculate the value n!. Don't use math module in this exercise.

while True:
    n = int(input("Provide n"))
    k = 1
    for i in range(1, n + 1):
        k = k * i
    print(k)
