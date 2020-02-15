from datetime import datetime,timedelta
from dateutil import tz

EDT = tz.gettz('America/New_York') 
CEST = tz.gettz('Europe/Warsaw') 

us_tzinfos = {'Central European Summer Time ': CEST,
              'Eastern Daylight Time ': EDT}

fmt = '%Y-%m-%d %H:%M:%S'
for itm in us_tzinfos:
    dt = datetime.now(us_tzinfos[itm])
    print(itm + str(dt.strftime(fmt)))
