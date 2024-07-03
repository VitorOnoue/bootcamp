from datetime import datetime, timezone, timedelta

date = datetime.now(timezone(timedelta(hours=2))) # oslo
print(date)
date = datetime.now(timezone(timedelta(hours=-3))) # sao paulo
print(date)