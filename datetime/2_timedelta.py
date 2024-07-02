from datetime import timedelta, datetime, time, date

car_size = "L" #small medium large
time_s = 30
time_m = 45
time_l = 60
date_now = datetime.now()
date_expected = date_now
match car_size:
    case "S":
        date_expected = date_now + timedelta(minutes=time_s)
    case "M":
        date_expected = date_now + timedelta(minutes=time_m)
    case "L":
        date_expected = date_now + timedelta(minutes=time_l)
        
print(f"car arrived on: {date_now}, expected to be ready on: {date_expected.date()}") # .date() on a datetime object returns the date only