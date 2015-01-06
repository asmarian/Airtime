import datetime
import time
from datetime import datetime, date, timedelta


start_minutes_from_now = datetime.now() -\
                         timedelta(days=2)
news = format(start_minutes_from_now, '%d')
print news