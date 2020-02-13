# Chocolate bar has the form of a rectangle divided into n×m portions. Chocolate bar can be split into two
# rectangular parts by breaking it along a selected straight line on its pattern. Determine whether it is possible to
# split it so that one of the parts will have exactly k squares.
#
# The program reads three integers: n, m, and k. It should print YES or NO.

n = int(input("row"))
m = int(input("column"))
k = int(input("squares"))

answer = False
for x in range(n):
    if x * m == k:
        answer = True
for y in range(m):
    if y*n == k:
        answer = True
if answer:
    print("YES")
else:
    print("NO")
