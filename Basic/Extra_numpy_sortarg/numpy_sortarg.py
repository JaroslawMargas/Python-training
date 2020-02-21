import numpy
# NumPy array and sorting
in_arr = numpy.array([2, 0, 1, 5, 4, 1, 9])
print("Input unsorted array : ", in_arr)

out_arr = numpy.argsort(in_arr)
print("Output sorted array indices : ", out_arr)
# [1 2 5 0 4 3 6]
# the smallest element is on:
# position 1 = 0
# pos2 = 1
# pos5 = 1
# pos0 = 2
# pos4 = 4
# pos3 = 5
# pos6 = 9
print("Output sorted array : ", in_arr[out_arr])

# Write a code to get the indices of N maximum values from a NumPy array.
ar = numpy.array([1, 3, 2, 4, 5, 6])
print(ar.argsort()[3:][::-1])
# [5 4 3]
