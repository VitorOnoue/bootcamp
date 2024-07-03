import pytz
from datetime import datetime

date = datetime.now(pytz.timezone("Europe/Oslo"))
print(date)
date = datetime.now(pytz.timezone("America/Sao_Paulo"))
print(date)