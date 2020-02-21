from functools import reduce


def do_sum(x1, x2):
    print(x1, x2)
    return x1 + x2


result = reduce(do_sum, [1, 2, 3, 4])
print(result)
# 1 2
# 3 3
# 6 4

# Result  10
