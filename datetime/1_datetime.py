from datetime import date, datetime # with this, theres no need to call the method with prefix (e.g., date.date.today())

print(date(2024, 7, 2))
print(date.today())

print(datetime(2024, 7, 2))
print(datetime.today())