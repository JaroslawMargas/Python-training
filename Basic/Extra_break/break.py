print("break loop")


def break_loop():
    for it in range(1, 5):
        if it == 2:
            return it
        print(it)
    return 5


print(break_loop())
# The return statement exits from a function, without executing the code that comes after it.
# 1,2
print("break all")


def break_all():
    for j in range(1, 5):  # 1,2
        for itm in range(1, 4):
            if itm * j == 6:  # 1*1,1*2,1*3,1*4 out/ 2*1,2*2,2*3 return (2) breake all loops
                return itm
            print(itm * j)


print(break_all())

# loop though both the elements of a list and have an index for the elements
print("enumerate index for the elements")
for index, item in enumerate(['one', 'two', 'three', 'four']):
    print(index, '::', item)

print("brake for")
for i in range(2):
    print(i)
    if i == 1:
        break
else:
    print('done')

print("if not break")
a = [1, 2, 3, 4]
for i in a:
    if type(i) is not int:
        print(i)
        break
else:
    print("no exception")
