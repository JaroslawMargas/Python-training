# ----with------try--finally-----------

# 1) without using with statement
file = open('file_path', 'w')
file.write('hello world !')
file.close()

# 2) without using with statement
file = open('file_path', 'w')
try:
    file.write('hello world')
finally:
    file.close()

# using with statement
with open('file_path', 'w') as file:
    file.write('hello world !')

# ---------try--finally-----------
try:
    print('operation_that_can_throw_ioerror')
except IOError:
    print('handle_the_exception_somehow')
else:
    # we don't want to catch the IOError if it's raised
    print('another_operation_that_can_throw_ioerror')
finally:
    print('something_we_always_need_to_do')