def make_list(n, m):
    list_val = []
    for i in range(n):
        print("row " + str(i))
        list_row = []
        for j in range(m):
            while True:
                try:
                    value = int(input("provide value for col " + str(j)))
                    list_row.append(value)
                    break
                except ValueError:
                    print("try again")

        list_val.append(list_row)
    print(list_val)
    return list_val


def swap_function(swap_array, swap, swap_to):
    for i in range(0, len(swap_array)):
        swap_array[i][swap], swap_array[i][swap_to] = swap_array[i][swap_to], swap_array[i][swap]

    print("swap")
    print(swap_array)


array_to_swap = []

while True:
    try:
        row = int(input("row number"))
        col = int(input("col number"))
        swap_col = int(input("col to swap: with range (0-n)"))
        swap_with_col = int(input("swap with column: range (0-n)"))
        if col > swap_col != swap_with_col < col:
            array_to_swap = make_list(row, col)
            swap_function(array_to_swap, swap_col, swap_with_col)
            break
        else:
            print("column value out of range or the same column value to swap")
    except ValueError:
        print("This value is incorrect")
