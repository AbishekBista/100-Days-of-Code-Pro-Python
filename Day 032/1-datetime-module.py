import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.weekday()
print(year, month, day)


date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)

print(date_of_birth)
