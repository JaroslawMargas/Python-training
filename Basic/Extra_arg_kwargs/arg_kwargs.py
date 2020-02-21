def my_func(form_arg, *args, **kwargs):
    print("formal arg:", form_arg)

    for arg in args:
        print("another arg:", arg)

    for key in kwargs:
        print("another keyword arg: %s: %s" % (key, kwargs[key]))
# or
    for key, value in kwargs.items():
        print("another keyword arg: %s: %s" % (key, value))


my_func(1, "one", "two ", myarg2="tree", myarg3=4)

# formal arg: 1
# another arg: one
# another arg: two
# another keyword arg: myarg2: tree
# another keyword arg: myarg3: 4
