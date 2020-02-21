# Function filtering for more then 0
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
# [-5, -4, -3, -2, -1]

# list of alphabets
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']


def filter_vowels(alphabet):
    vowels = ['a', 'r', 'i', 'o', 'u']

    if alphabet in vowels:
        return True
    else:
        return False


filtered_vowels = filter(filter_vowels, alphabets)
list_vowels = list(filtered_vowels)

print(list_vowels)
# ['a', 'e', 'i', 'o']
