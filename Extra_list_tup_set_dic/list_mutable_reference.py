# try to change reference list

def try_to_change_list_reference(the_list):
    print('got in ref function', the_list)
    the_list = ['5', '6', '7', '8', '9']
    print('set to', the_list)


outer_list = ['1', '2', '3', '4']
print('before, outer_list =', outer_list)
try_to_change_list_reference(outer_list)
print('after, outer_list =', outer_list)


# before, outer_list = ['1', '2', '3', '4']
# got in ref function ['1', '2', '3', '4']
# set to ['5', '6', '7', '8', '9']
# after, outer_list = ['1', '2', '3', '4']
