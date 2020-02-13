# Write a code to sort a numerical list in Python

list_to_sort = ["2", "5", "7", "8", "1"]
# cast to int in loop
list_to_sort = [int(i) for i in list_to_sort]
# sort
list_to_sort.sort()
print(list_to_sort)
