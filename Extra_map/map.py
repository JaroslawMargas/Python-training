# What is a map function in Python?

# The map() function in Python has two parameters, function and iterable. The map() function takes a function as an
# argument and then applies that function to all the elements of an iterable, passed to it as another argument. It
# returns an object list of results.

def calculate_sq(n):
    return n * n


numbers = (2, 3, 4, 5)
result = map(calculate_sq, numbers)
print(list(result))

