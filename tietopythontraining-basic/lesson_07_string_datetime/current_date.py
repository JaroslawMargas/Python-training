# pip install pytz
import datetime
import pytz

# now(tz=None) - return the current local date and time
# utcnow() - return the current UTC date and time, with tzinfo None.

data_time_now = datetime.datetime.now(tz=None)
display_format = "%Y-%b-%d %H:%M:%S %Z%z"

# change timezone IST+0530
server_timezone = pytz.timezone("Asia/Kolkata")
data_time_Asia = data_time_now.now(server_timezone)

print(data_time_Asia)
# 2019-10-06 22:57:27.366587+05:30

print(data_time_Asia.strftime(display_format))
# 2019-Oct-06 22:57:27 IST+0530

date = data_time_Asia.date()
print(date)
# 2019-10-06
print(date.year)
# 2019
print(date.month)
# 10
print(date.day)
# 6

time = data_time_Asia.time()
print(time)
# 22:57:27.366587
print(time.hour)
# 22
print(time.minute)
# 57
print(time.second)
# 27


# %a	Locale's abbreviated weekday name.
# %A	Locale's full weekday name.
# %b	Locale's abbreviated month name.
# %B	Locale's full month name.
# %c	Locale's appropriate date and time representation.
# %d	Day of the month as a decimal number [01,31].
# %H	Hour (24-hour clock) as a decimal number [00,23].
# %I	Hour (12-hour clock) as a decimal number [01,12].
# %j	Day of the year as a decimal number [001,366].
# %m	Month as a decimal number [01,12].
# %M	Minute as a decimal number [00,59].
# %p	Locale's equivalent of either AM or PM.	(1)
# %S	Second as a decimal number [00,61].	(2)
# %U	Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new
#       year preceding the first Sunday are considered to be in week 0.	(3)
# %w	Weekday as a decimal number [0(Sunday),6].
# %W	Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new
#       year preceding the first Monday are considered to be in week 0.	(3)
# %x	Locale's appropriate date representation.
# %X	Locale's appropriate time representation.
# %y	Year without century as a decimal number [00,99].
# %Y	Year with century as a decimal number.
# %Z	Time zone name (no characters if no time zone exists).
# %%	A literal "%" character.
