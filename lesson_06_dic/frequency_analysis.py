# Given a number n, followed by n lines of text, print all words encountered in the text, one per line. The words
# should be sorted in descending order according to their number of occurrences in the text, and all words with the
# same frequency should be printed in lexicographical order.
#
# Hint. After you create a dictionary of the words and their frequencies, you would like to sort it according to the
# frequencies. This can be achieved if you create a list whose elements are tuples of two elements: the frequency of
# occurrence of a word and the word itself. For example, [(2, 'hi'), (1, 'what'), (3, 'is')]. Then the standard list
# sort will sort a list of tuples, with the tuples compared by the first element, and if these are equal,
# by the second element. This is nearly what is required in the problem.

import operator
line_nr = int(input("Now many text line ?"))
dict_word = dict()

for i in range(line_nr):
    *line_list, = input().split()
    for word in line_list:
        if word not in dict_word:
            # if not exist in dictionary add and set value to 1
            dict_word.setdefault(word, 1)
        else:
            # get value of frequency and +1
            val = dict_word[word]
            dict_word[word] = val+1

# reverse sorting
sorted_dict = sorted(dict_word.items(), key=operator.itemgetter(1), reverse=True)

for key, freq in sorted_dict:
    print("the key {} has a frequency {}".format(key, freq))

