from datetime import datetime

while True :
    try :
        N = int(input("timestamp ?"))
        display_format = "%Y-%b-%d %H:%M:%S %Z%z"
        date = datetime.fromtimestamp(N)
        print(date.strftime(display_format))
    except (ValueError, OSError, OverflowError) as er:
        print(repr(er))
