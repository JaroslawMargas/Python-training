from datetime import datetime, timedelta
from dateutil import tz

# TimeZone
timeZone_Warsaw = tz.gettz('Europe/Warsaw')

wa_time = datetime.now(timeZone_Warsaw)
# fmt = '%Y-%m-%d %H:%M:%S %Z%z'
fmt = '%Y-%m-%d %H:%M:%S'
print("Warsaw " + str(wa_time.strftime(fmt)))


# Delay
def get_days(date_format, add_days):
    after = wa_time + timedelta(days=add_days)
    return after.strftime(date_format)


day_delay = 12
new_fmt = '%Y-%m-%d'
dt = get_days(new_fmt, day_delay)
print("After: " + str(day_delay) + " days will be: " + dt)
