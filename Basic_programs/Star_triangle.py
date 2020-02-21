def py_func(r):
    for x in range(r):
        print(' ' * (r - x - 1) + '*' * (2 * x + 1))
        # empty * 9-0-1 = 8 + * (2*0+1) = 1


py_func(9)
