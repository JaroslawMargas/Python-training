# Given two integers representing the rows and columns (m×n), and subsequent m rows of n elements, find the index
# position of the maximum element and print two numbers representing the index (i×j) or the row number and the column
# number. If there exist multiple such elements in different rows, print the one with smaller row number. If there
# multiple such elements occur on the same row, output the smallest column number.

list_val_test = [[0, 3, 2, 4],
                 [2, 3, 5, 5, ],
                 [5, 1, 2, 3, ]]


def make_list(n, m):
    list_val = []
    for i in range(n):
        print("row " + str(i))
        list_row = []
        for j in range(m):
            while True:
                try:
                    value = int(input("provide value for col "+str(j)))
                    list_row.append(value)
                    break
                except ValueError:
                    print("try again")

        list_val.append(list_row)
    return list_val


def check_max(check_list):
    max_val = 0
    max_col = 0
    max_row = 0

    rows = 0
    for i in check_list:
        cols = 0
        for j in i:
            if max_val < j:
                max_val = j
                max_row = rows
                max_col = cols
            cols += 1
        rows += 1

    print("max val is " + str(max_val) + " in col " + str(max_col) + " and row " + str(max_row))


while True:
    try:
        row = int(input("row number"))
        col = int(input("col number"))
        break
    except ValueError:
        print("This value is incorrect")

list_res = make_list(row, col)
print(list_res)
check_max(list_res)
