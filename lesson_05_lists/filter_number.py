# list_of_strings = ['2', '0', '8', '3']
# to_filter_range = range(3)
# expected_output = [8, 3]

list_of_strings = ['2', '0', '8', '3']

print([str(x) for x in list_of_strings if int(x) not in range(3)])

# filter usage
val = 3
def function(arg):
    if int(arg) >= val:
        return True
    else:
        return False


print(list(filter(function, list_of_strings)))

# lambda usage
print(list(filter(lambda x: int(x) >= val, list_of_strings)))
