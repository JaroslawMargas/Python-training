def f(x, list_arg=[]):
    for x in range(x):
        list_arg.append(x * x)
    print(list_arg)


f(2)
f(3, [3, 2, 1])
f(3)

# [0, 1]
# [3, 2, 1, 0, 1, 4]
# [0, 1, 0, 1, 4]

# the same as

l_mem = []

l = l_mem  # the first call
for i in range(2):
    l.append(i * i)

print(l)  # [0, 1]

# there is created new list
l = [3, 2, 1]  # the second call
for i in range(3):
    l.append(i * i)

print(l)  # [3, 2, 1, 0, 1, 4]

# new list use the memory from previous list l_mem
l = l_mem  # the third call
for i in range(3):
    l.append(i * i)

print(l)  # [0, 1, 0, 1, 4]



