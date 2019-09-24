while True:
    try:
        input_str = input()
        N, K = input_str.split()
        pin_status = ['I'] * int(N)
        print(''.join(pin_status))
        break
    except ValueError:
        print("no proper value")

for i in range(int(K)):
    while True:
        try:
            data = input()
            n, k = data.split()
            for j in range(int(n) - 1, int(k)):
                pin_status[j] = '.'
                print(' '.join(pin_status))
            break
        except ValueError:
            print("no enough value, ball will lost")
            break
        except IndexError:
            print("pin is out of range")
            break
print(" State of pins")
print(''.join(pin_status))
