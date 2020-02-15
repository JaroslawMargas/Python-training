def try_to_change_list_contents(the_list):
    print('got append', the_list)
    the_list.append('D')
    print('changed to', the_list)


outer_list = ['A', 'B', 'C']

print('before, outer_list =', outer_list)
try_to_change_list_contents(outer_list)
print('after, outer_list =', outer_list)

# before, outer_list = ['A', 'B', 'C']
# got append ['A', 'B', 'C']
# changed to ['A', 'B', 'C', 'D']
# after, outer_list = ['A', 'B', 'C', 'D']
