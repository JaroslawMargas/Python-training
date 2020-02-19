def f2(arg1, arg2, *args, **kwargs):
    print("argument: {0},{1} ".format(arg1, arg2))
    for itm in args:
        print("args: {0} ".format(itm))

    for key, value in kwargs.items():
        print("kwargs: {0}:{1} ".format(key, value))


l = [1, 2, 3]
d = {'a': 7, 'b': 8, 'c': 9}

f2(*l, **d)

# argument: 1,2
# args: 3
# kwargs: a:7
# kwargs: b:8
# kwargs: c:9
