import time


# 0 	1 	1 	2 	3 	5 	8 	13 	21 	34 	55 	89 	144 	233 	377 	610 	987 	1597 	2584 	4181

# loop

def fib_loop(m):
    b = 1
    a = 0
    sum_fib = 0
    if m < 0:
        raise Exception('Negative value')
    else:
        for x in range(m):
            if x == 0:
                sum_fib == 0
            else:
                b = b + a
                a = b - a
                sum_fib += a
        return sum_fib


# recursion

def fib_recursion(n):
    if n < 3:
        return 1
    return fib_recursion(n - 1) + fib_recursion(n - 2)


if __name__ == '__main__':
    num_in = int(input('Enter number\n'))
    # print(fib_recursion(num_in))
    print("Sum: "+str(fib_loop(num_in)))
