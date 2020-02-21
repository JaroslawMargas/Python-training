my_str = "Hello!!!, h{e said ---and went."

punctuations = "'!()-[]{};:'\"\,<>./?@#$%^&*_~"


def remove_punctuations(my_str_to_remove):
    for x in my_str_to_remove:
        if x not in punctuations:
            return True
        else:
            return False


str1 = ""
result = filter(remove_punctuations, my_str)
for ele in result:
    str1 += ele
print(str1)

# # define punctuation
# punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
# my_str = "Hello!!!, he said ---and went."
# # To take input from the user
# # my_str = input("Enter a string: ")
# # remove punctuation from the string
# no_punct = ""
# for char in my_str:
#     if char not in punctuations:
#         no_punct = no_punct + char
# # display the unpunctuated string
# print(no_punct)
