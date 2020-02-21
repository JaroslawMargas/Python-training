# SET MUTABLE, UNORDERED , UNINDEXED, NO DUPLICATE

a = "Hello"

# convert string to set()
set_structure = set(a)

print(set_structure)  # l is removed
# set(['h', 'e', 'l', 'o'])

# sorting
someList = [5, 2, 3, 4]

e = set(someList)
print(e)
# set([2, 3, 4, 5])

# add new element

e.add(int(6))
print(e)
# {2, 3, 4, 5, 6}

# add multiple items

e.update([7, 8, 9])
print(e)
# {2, 3, 4, 5, 6, 7, 8, 9}

# remove or discard

# e.remove(10)  --> KeyError: 10
e.discard(10)  # --> will NOT raise error
print(e)

# iteration
for itm in set_structure:
    print(itm)
# UNORDERED VALUE
# H
# l
# o
# e

# Length
print(len(set_structure))
# 4 without duplicate

# fast membership testing
print('H' in set_structure)
# True


cities = frozenset(["Frankfurt", "Basel","Freiburg"])
# cities.add("Strasbourg")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'frozenset' object has no attribute 'add'