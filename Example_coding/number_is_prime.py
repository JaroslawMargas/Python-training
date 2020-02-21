a = int(input("enter number"))
if a > 1:
    if (a % 2) == 0:
        print("not prime")
    else:
        print("Prime")
else:
    print("not prime")


def print_prime(n):
    for i in range(1, n):
        if not i % 2 == 0:
            print(i)


print_prime(10)
