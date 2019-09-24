def col_check(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


if __name__ == '__main__':
    try:
        val = int(input('Enter number:'))
        while True:
            val = col_check(val)
            if val == 1:
                break

    except ValueError:
        print('No proper value')
