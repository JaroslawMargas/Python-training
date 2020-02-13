import re

Substring = 'string'

String = '''We are learning regex with geeksforgeeks  
         regex is very useful for string matching. 
          It is fast too.'''

print(re.match(Substring, String, re.IGNORECASE))

result = re.search(Substring, String, re.IGNORECASE)
print(result.span())

# find in (77, 83)

# re.match() searches only in the first line of the string
# re.search() searches for the whole string
