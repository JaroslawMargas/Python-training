# Given a number n, followed by n lines of text, print the number of distinct words that appear in the text.
#
# For this, we define a word to be a sequence of non-whitespace characters, seperated by one or more whitespace or
# newline characters. Punctuation marks are part of a word, in this definition.

string = 'She sells sea shells on the sea shore; The shells that she sells are sea shells I\'m sure. So if she sells ' \
         'sea shells on the sea shore, I\'m sure that the shells are sea shore shells. '

split_string = string.split()
word_set = set()
for i in split_string:
    word_set.add(i)
print(len(word_set))