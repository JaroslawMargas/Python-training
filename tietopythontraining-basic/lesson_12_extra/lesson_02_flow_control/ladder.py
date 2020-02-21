# For given integer n ≤ 9 print a ladder of n steps. The k-th step consists of the integers from 1 to k without
# spaces between them.
#
# To do that, you can use the sep and end arguments for the function print().

n = int(input("provide n"))\

ladder_str = ""
for x in range(1, n+1):
    ladder_str = ladder_str + str(x)
    print(ladder_str)
