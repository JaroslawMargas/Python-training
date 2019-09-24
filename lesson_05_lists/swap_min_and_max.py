list_number = list([int(s) for s in input().split()])

min_index = list_number.index(min(list_number))
max_index = list_number.index(max(list_number))

min_val = list_number[min_index]

list_number[min_index] = list_number[max_index]
list_number[max_index] = min_val

print(list_number)