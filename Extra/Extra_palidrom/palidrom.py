# Write a Python program to check whether a given string is a palindrome or not, without using an iterative method.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam, nurses run.

def fun(string):
    string_reverse = string[::-1]
    if string == string_reverse:
        return True
    else:
        return False


print(fun("madam"))
