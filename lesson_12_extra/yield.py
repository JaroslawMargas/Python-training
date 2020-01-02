def gen_func():
    for itm in 'abc':
        yield itm


lt = gen_func()
print(list(lt))

# ['a', 'b', 'c']

# The yield statement works differently than return - it returns the value and suspends the function, but does not
# leave it.