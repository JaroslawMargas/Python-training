# Largest with numpy
import numpy

num1 = 10
num2 = 14
num3 = 12

array = numpy.array([num1, num2, num3])
out_array = numpy.argsort(array)
print(array[out_array][::-1][0])
# 14