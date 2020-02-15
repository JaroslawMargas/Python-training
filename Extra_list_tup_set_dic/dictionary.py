# dictionaries is MUTABLE, unordered, changeable, indexes

dictionary = {
    '1': 'one',
    '2': 'two',
    '3': 'tree'
}

# value
x = dictionary['1']
print(x)
# one

# value get()
y = dictionary.get('2')
print(y)
# two

# get keys
print(dictionary.keys())
# dict_keys(['1', '2', '3'])

# get values
print(dictionary.values())
# dict_values(['one', 'two', 'tree'])

# iteration through key and value
for key, value in dictionary.items():
    print(key, "::", value)

# delete del
del dictionary['3']
print(dictionary)
# {'1': 'one', '2': 'two'}

# delete pop return default if not exist
pop_default = dictionary.pop('5', 'fife')
print(pop_default)
# fife
