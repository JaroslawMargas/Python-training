def test_var_args(f_arg, *argv, **kwargs) :
    print("first normal arg:", f_arg)
    for arg in argv :
        print("another arg :", arg)

    for key, value in kwargs.items() :
        print("{0} = {1}".format(key, value))


test_var_args('yasoob', 'python', 'eggs', 'test_fun', name="Jan", surname="Nowak")
