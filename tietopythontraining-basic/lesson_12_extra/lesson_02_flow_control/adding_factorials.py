# Given an integer n, print the sum_val 1!+2!+3!+...+n!.
#
# This problem has a solution with only one loop, so try to discover it. And don't use the math library :)

while True:
    n = int(input("Provide n"))
    k = 1
    sumK = 0
    for i in range(1, n + 1):
        k = k * i
        sumK = sumK + k
    print(sumK)
