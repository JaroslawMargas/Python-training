print((1, 2) + (3, 4))
# (1, 2, 3, 4)

names = "{1}, {2} and {0}".format('John', 'Bill', 'Sean')
print(names)
# Bill, Sean and John

n = [x * x for x in range(4)]
print(n)
# [0, 1, 4, 9]

squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares.pop(4))
print(squares)
# remove the element with key =4 and return value = 16
# 16
# {1: 1, 2: 4, 3: 9, 5: 25}