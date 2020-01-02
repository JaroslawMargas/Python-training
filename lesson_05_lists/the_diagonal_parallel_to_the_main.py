def make_list(n):
    list_val = []
    for i in range(n):
        list_row = []
        for count in range(n):
            value = abs(i - count)
            list_row.append(value)
            count += 1
        list_val.append(list_row)
    print(list_val)
    return list_val


def make_list2(n):
    print([[abs(x - count) for x in range(n)] for count in range(n)])


make_list(5)

# [[0, 1, 2, 3, 4], [1, 0, 1, 2, 3], [2, 1, 0, 1, 2], [3, 2, 1, 0, 1], [4, 3, 2, 1, 0]]
