# list_of_strings = ['2', '0', '8', '3']
# to_filter_range = range(3)
# expected_output = [8, 3]

list_of_strings = ['2', '0', '8', '3']

print([int(x) for x in list_of_strings if int(x) not in range(3)])
