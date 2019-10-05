text = str(input("Input text:"))

# remove comma and dot from text.
text = text.replace(',', '')
text = text.replace('.', '')

# this function is working if there is not space at the beginning/end of the string
text_count = text.count(" ")+1
print("count function: "+str(text_count))

# split text to list
split_text = text.split(" ")

# make a filter for empty (space at the beginning of the string is taking from split function)
str_list = list(filter(None, split_text))

word_repetition = list(set(str_list))

word_count = len(str_list)
word_count_repetition = len(word_repetition)

print("words: "+str(word_count))
print("words without repetition: "+str(word_count_repetition))
