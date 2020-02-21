# Tuple IMMUTABLE ,unchanged,  ordered, indexes , allow duplicate

# tuple value can NOT be changed
tuple_collection = ("a", "b", "c")
print("this is a tuple: " +str(tuple_collection))
# tuple_collection[0] = "A"
# TypeError: 'tuple' object does not support item assignment

# indexed
print("Index 0:"+tuple_collection[0])
# a

print("Convert tuple to list")
# convert tuple -> list -> tuple
list_collection = list(tuple_collection)
print(list_collection)
print("Change value in list")
list_collection[0] = "A"
print(list_collection)
print("Convert list to tuple")
tup = tuple(list_collection)
print(tup)

# get value
print("Print value:")
a, b, c = tuple_collection
print(a, b, c)
