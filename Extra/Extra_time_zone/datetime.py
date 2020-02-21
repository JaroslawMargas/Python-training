# str() displays today date in a way that the user can understand the date and time repr() prints official
# representation of a datetime object (means using the official string representation we can reconstruct the object

import datetime

today = datetime.datetime.now()
a = str(today)
print(today)
# 2018-10-15 17:58:07.393000

b = repr(today)
print(b)
# datetime.datetime(2018, 10, 15, 17, 58, 7, 393000)

# str() is used for creating output for end user 
# repr() is mainly used for debugging and development. reprs goal is to be unambiguous and strs is to be readable
print(str(2.0 / 11.0))
# 0.181818181818
print(repr(2.0 / 11.0))
# 0.18181818181818182
