def fib_loop(m):
    b = 1
    a = 0
    sum_fib = 0
    if m < 0:
        raise Exception('Negative value')
    else:
        for x in range(m):
            if x == 0:
                sum_fib = 0
            else:
                b = b + a
                a = b - a
                sum_fib += a
        return sum_fib


print(fib_loop(7))
