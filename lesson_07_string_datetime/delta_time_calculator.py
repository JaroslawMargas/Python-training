import datetime

now = datetime.datetime.now()

display_format = "%d %b %Y %H:%M:%S"
print(now.strftime(display_format))

while True :
    try :
        year = int(input("year:"))
        month = int(input("month:"))
        day = int(input("day:"))
        break
    except ValueError :
        print("no proper value")

feature_date = datetime.datetime(year, month, day)

delta = feature_date - now

seconds_in_date = delta.total_seconds()

days = divmod(seconds_in_date, 86400)
hours = divmod(days[1], 3600)
minutes = divmod(hours[1], 60)
seconds = divmod(minutes[1], 1)
print("Time difference: %d days, %d hours, %d minutes and %d seconds" % (days[0], hours[0], minutes[0], seconds[0]))

