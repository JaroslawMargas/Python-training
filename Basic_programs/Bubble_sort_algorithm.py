def bs(sort_value):  # a = name of list
    b = len(sort_value) - 1  # minus 1 because we always compare 2 adjacent values

    for x in range(b):
        for y in range(b - x):
            if sort_value[y] > sort_value[y + 1]:
                sort_value[y], sort_value[y + 1] = sort_value[y + 1], sort_value[y]
                print(sort_value[y], sort_value[y + 1] )
    return sort_value


a = [32, 5, 3, 6, 7, 54, 87]
bs(a)
print(a)