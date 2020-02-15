# String - an IMMUTABLE type

outer_string = 'abcd'


def try_to_change_string_reference(the_string):
    print('got', the_string)
    the_string = 'ghij'
    print('set to', the_string)


print('before, outer_string ', outer_string)
try_to_change_string_reference(outer_string)
print('after, outer_string =', outer_string)

a = 'hello'

b = list(a)
print(b)
# ['h', 'e', 'l', 'l', 'o']

c = tuple(a)
print(c)
# ('h', 'e', 'l', 'l', 'o')

d = set(a)
print(d)  # l is removed !! because no duplicate in SET()
# set(['h', 'e', 'l', 'o'])
