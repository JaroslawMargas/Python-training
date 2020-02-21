# -----sort---vs-----sorted----------

# list.sort mutates the list in-place & returns None
# sorted takes any iterable & returns a new list, sorted.
# Use list.sort() when you want to mutate the list, sorted() when you want a new sorted object back.
# Use sorted() when you want to sort something that is an iterable, not a list yet.

list_to_sort = [3, 2, 4, 1]

print(list_to_sort.sort())
# None !!!
print(list_to_sort)
# [1, 2, 3, 4]

list_to_sort2 = [3, 2, 4, 1]

print(sorted(list_to_sort2))
# [1, 2, 3, 4]