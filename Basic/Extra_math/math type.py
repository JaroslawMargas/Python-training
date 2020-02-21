import operator
import math
from operator import truediv

a, b, c, d, e = 3, 2, 2.0, -3, 10

print(a / b)
# a int / b int = c int  3/2 =1

print(a / (b * 1.0))
# a int / b float = c float 3/2.0 = 1,5

print(truediv(a, b))
# 1.5

print(a // b)
# 3/2 = 1
print(a // c)
# 3/2.0 =1.0

print(operator.add(a, b))
# 3+2 =5

print(b ** a)
# = 2*2*2 =2"3 = 8
print(pow(b, a))
# 8

x = 8
print(x ** 1 / 3)
print(math.pow(x, 1 / 3))
