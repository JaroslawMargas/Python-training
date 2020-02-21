def gen_func():
    for itm in 'abc':
        yield itm


lt = list(gen_func())
print(lt)


# ['a', 'b', 'c']

# The yield statement works differently than return - it returns the value and suspends the function, but does not
# leave it.

def next_square():
    i = 1

    while True:
        yield i * i
        i += 1


for num in next_square():
    if num > 100:
        break
    print(num)
